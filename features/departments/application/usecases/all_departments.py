from features.departments.infrastructure.department_repository import DepartmentRepository
from features.departments.application.contracts.response_contract import DepartmentResponseContract
class AllDepartmentUseCase:

    def __init__(self, repo : DepartmentRepository):
        self.repo = repo

    def execute(self)->list[DepartmentResponseContract]:
        
        departments = self.repo.all();

        return [
            DepartmentResponseContract(
                id=department.id,
                department_id=department.department_id,
                department_name=department.department_name,
                room_id=department.room_id,
                room=department.room,
            )
            for department in departments
        ]