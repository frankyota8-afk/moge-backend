from features.departments.infrastructure.department_repository import DepartmentRepository
from features.departments.application.contracts.getById_contract import GetByIdContract
from features.departments.application.contracts.response_contract import DepartmentResponseContract

from features.departments.domain.department_entity import DepartmentEntity

class GetByIdUseCase:
    
    def __init__(self ,repo : DepartmentRepository):
        self.repo = repo

    def execute(self, contract : GetByIdContract)->DepartmentResponseContract:

        entity = DepartmentEntity(
            id=contract.id
        )

        entity = self.repo.getById(entity)

        return DepartmentResponseContract(
            id=entity.id,
            department_id=entity.department_id,
            department_name=entity.department_name,
            room_id=entity.room_id,
            room=entity.room,
        )
