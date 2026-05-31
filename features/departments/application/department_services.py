from features.departments.application.contracts.response_contract import DepartmentResponseContract
from features.departments.infrastructure.department_repository import DepartmentRepository
from features.departments.application.usecases.all_departments import AllDepartmentUseCase
from features.departments.application.usecases.create_department import DepartmentCreateUseCase
from features.departments.application.usecases.delete_department import DepartmentDeleteUseCase
from features.departments.application.usecases.update_department import DepartmentUpdateUseCase
from features.departments.application.contracts.create_contract import DepartmentCreateContract
from features.departments.application.contracts.update_contract import DepartmentUpdateContract
from features.departments.application.contracts.delete_contract import DepartmentDeleteContract
from features.departments.application.usecases.getByColumn_usecase import GetByColumnUseCase
from features.departments.application.contracts.getByColumn_contract import GetByColumnContract
from features.departments.application.usecases.getById_usecase import GetByIdUseCase
from features.departments.application.contracts.getById_contract import GetByIdContract
class DepartmentServices:

    def __init__(self, repo : DepartmentRepository):
        self.all_departments_usecase = AllDepartmentUseCase(repo=repo)
        self.create_departments_usecase = DepartmentCreateUseCase(repo=repo)
        self.update_departments_usecase = DepartmentUpdateUseCase(repo=repo)
        self.delete_departments_usecase = DepartmentDeleteUseCase(repo=repo)
        self.getById_usecase = GetByIdUseCase(repo=repo)
        self.getByColumn_usecase = GetByColumnUseCase(repo=repo)
        
        

    def allDepartments(self)->list[DepartmentResponseContract]:
        return self.all_departments_usecase.execute()
    
    def creatDepartment(self, contract : DepartmentCreateContract)->DepartmentResponseContract:
        return self.create_departments_usecase.execute(contract=contract)
    
    def updateDepartment(self, contract : DepartmentUpdateContract):
        return self.update_departments_usecase.execute(contract=contract)
    
    def deleteDepartment(self, contract : DepartmentDeleteContract):
        return self.delete_departments_usecase.execute(contract)
    
    def getDepartmentbyColumn(self, contract: GetByColumnContract)->list[DepartmentResponseContract]:
        return self.getByColumn_usecase.execute(contract=contract)
    
    def getDepartmentbyId(self, contract: GetByIdContract)->DepartmentResponseContract:
        return self.getById_usecase.execute(contract=contract)
