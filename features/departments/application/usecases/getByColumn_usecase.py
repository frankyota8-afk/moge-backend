from features.departments.infrastructure.department_repository import DepartmentRepository
from features.departments.application.helpers.department_helper import contractToEntity
from features.departments.application.contracts.response_contract import DepartmentResponseContract
from features.departments.application.contracts.getByColumn_contract import GetByColumnContract

class GetByColumnUseCase:
    
    def __init__(self, repo : DepartmentRepository):
        self.repo = repo

    def execute(self, contract : GetByColumnContract)->list[DepartmentResponseContract]:
        
        entity = contractToEntity(contract)

        departments = self.repo.getByColumn(entity)

        return [
            DepartmentResponseContract(
                id=department.id,
                department_id=department.department_id,
                department_name=department.department_name,
                room_id=department.room_id,
                room=department.room
            )
            for department in departments
        ]
        