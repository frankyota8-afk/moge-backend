from features.departments.infrastructure.department_repository import DepartmentRepository
from features.departments.domain.department_entity import DepartmentEntity
from features.departments.application.contracts.update_contract import DepartmentUpdateContract
from features.departments.application.contracts.response_contract import DepartmentResponseContract

class DepartmentUpdateUseCase:

    def __init__(self  , repo : DepartmentRepository):
        self.repo = repo

    def execute(self, contract : DepartmentUpdateContract):

        entity = DepartmentEntity(
            id=contract.id,
            department_id=contract.department_id,
            department_name=contract.department_name,
            room_id=contract.room_id if contract.room_id else None
        )

        result = self.repo.update(entity=entity)

        if result is None:
            message = "Failed to update!"
        else:
            message = "Updated Successfully!"

        return DepartmentResponseContract(
            department_id=result.department_id,
            department_name=result.department_name,
            room_id=result.room_id,
            room=result.room,
        ), message

        

        
