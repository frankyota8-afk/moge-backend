from features.departments.infrastructure.department_repository import DepartmentRepository
from features.departments.domain.department_entity import DepartmentEntity
from features.departments.application.contracts.create_contract import DepartmentCreateContract
from features.departments.application.contracts.response_contract import DepartmentResponseContract

class DepartmentCreateUseCase:

    def __init__(self  , repo : DepartmentRepository):
        self.repo = repo

    def generateID(self):

        last_department = self.repo.last_row()
        if last_department and last_department.department_id:

            last_number = int(last_department.department_id.split("-")[1])
            new_number = last_number + 1
        else:
            new_number = 1

        return f"DPMT-{new_number:03d}"


    def execute(self, contract : DepartmentCreateContract):

        entity = DepartmentEntity(
            department_id=self.generateID(),
            department_name=contract.department_name,
            room_id=contract.room_id if contract.room_id else None
        )

        entity = self.repo.create(entity=entity)

        response = DepartmentResponseContract(
            id = entity.id,
            department_id=entity.department_id,
            department_name=entity.department_name,
            room_id=entity.room_id
        )

        return response

        

        
