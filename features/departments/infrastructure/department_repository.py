# features/departments/infrastructure/department_repository.py
from typing import List, Optional
from features.departments.domain.department_entity import DepartmentEntity
from features.departments.models import Department
from features.departments.infrastructure.department_mapper import DepartmentMapper
from features.departments.domain.exceptions import RepositoryException
from features.departments.application.helpers.department_helper import remove_noneValues

class DepartmentRepository:

    # --------------------
    # GET ALL
    # --------------------
    @staticmethod
    def all() -> List[DepartmentEntity]:
        departments = Department.objects.select_related("room").all()
        return [
            DepartmentMapper.toEntity(data=department)
            for department in departments
        ]

    # --------------------
    # GET BY ID
    # --------------------
    @staticmethod
    def getById(entity: DepartmentEntity) -> Optional[DepartmentEntity]:
        try:
            department = Department.objects.select_related("room").get(id=entity.id)
        except Department.DoesNotExist:
            return None

        return DepartmentMapper.toEntity(data=department)

    # --------------------
    # CREATE
    # --------------------
    @staticmethod
    def create(entity: DepartmentEntity) -> DepartmentEntity:
        model_data = DepartmentMapper.toModel(entity)

        department = Department.objects.create(**model_data)

        return DepartmentMapper.toEntity(data=department)

    # --------------------
    # UPDATE
    # --------------------
    @staticmethod
    def update(entity: DepartmentEntity) -> Optional[DepartmentEntity]:
        model_data = DepartmentMapper.toModel(entity)
        try:
            row = Department.objects.filter(id=entity.id).update(**model_data)
            print("this is update department data:",row)
            if row == 0:
                return None
            
            department = Department.objects.select_related("room").get(id=entity.id)
            return department
        
        except Exception as e:
            raise RepositoryException(str(e))
    
    
    # --------------------
    # DELETE
    # --------------------
    @staticmethod
    def delete(entity: DepartmentEntity) -> bool:
        try:
            department = Department.objects.get(id=entity.id)
        except Department.DoesNotExist:
            return False

        department.delete()
        return True
    
    # --------------------
    # LAST ROW
    # --------------------
    @staticmethod
    def last_row() -> Department:
        department = Department.objects.order_by("-id").first()
        return department
    
    @staticmethod
    def getByColumn(entity: DepartmentEntity)->list[DepartmentEntity]:
        
        model_data = remove_noneValues(DepartmentMapper.toModel(entity))
        
        departments = Department.objects.select_related("room").filter(**model_data)

        return [
            DepartmentMapper.toEntity(department)
            for department in departments
        ]
