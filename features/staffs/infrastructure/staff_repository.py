from features.staffs.models import Staff
from features.staffs.infrastructure.staff_mapper import StaffMapper
from features.staffs.domain.staff_entity import StaffEntity
from features.staffs.domain.exceptions import RepositoryException
from features.shared.helpers.helper import removeNoneValue

class StaffRepository:

    @staticmethod
    def create(entity: StaffEntity)->StaffEntity:
        model_data = StaffMapper.toModel(entity)
        try:
            instance = Staff.objects.create(**model_data)
            return StaffMapper.toEntity(instance)
        except Exception as e:
            raise RepositoryException(str(e))
        
    def all()->list[StaffEntity]:
        try:
            staffs = Staff.objects.select_related("department","role","rank","stype").all()
            return [
                StaffMapper.toEntity(s)
                for s in staffs
            ]
        except Exception as e:
            raise RepositoryException(str(e))
        
    def getByEmail(email)->StaffEntity:
        instance = Staff.objects.select_related(
            "department", "role", "rank", "stype"
        ).filter(staff_email=email).first()
        return instance
    
    def getById(entity: StaffEntity)->StaffEntity:
        staff = Staff.objects.select_related(
            "department", "role", "rank", "stype"
        ).get(id=entity.id)

        return StaffMapper.toEntity(staff)
        
    def getByColumn(entity: StaffEntity)->list[StaffEntity]:
        try:
            model_data = removeNoneValue(StaffMapper.toModel(entity))
            staffs = Staff.objects.select_related(
                "department", "role", "rank", "stype"
            ).filter(**model_data)

            return [
                StaffMapper.toEntity(s)
                for s in staffs
            ]
        except Exception as e:
            raise RepositoryException(str(e))

    def update(entity: StaffEntity)->bool:
        
        model_data = StaffMapper.toModel(entity)
        row = Staff.objects.filter(id=entity.id).update(**model_data)
        staff = Staff.objects.get(id=entity.id)
        return staff
    
    def delete(entity: StaffEntity)->bool:
        row,_ = Staff.objects.get(id=entity.id).delete()

        return row > 0
            

