from features.departments.infrastructure.department_repository import DepartmentRepository
from features.departments.domain.department_entity import DepartmentEntity
from features.departments.application.contracts.delete_contract import DepartmentDeleteContract
from features.departments.application.contracts.response_contract import DepartmentResponseContract

class DepartmentDeleteUseCase:

    def __init__(self  , repo : DepartmentRepository):
        self.repo = repo

    def execute(self, contract : DepartmentDeleteContract)->str:

        entity = DepartmentEntity(
            id=contract.id
        )

        status = self.repo.delete(entity)

        if status:
            message = "Deleted successfully!"
        else:
            message = "Failed to delete"

        return message

        

        
