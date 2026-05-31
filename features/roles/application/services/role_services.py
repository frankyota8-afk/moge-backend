from features.roles.application.usecases.create_usecase import CreateUseCase
from features.roles.application.usecases.update_usecase import UpdateUseCase
from features.roles.application.usecases.delete_usecase import DeleteUseCase
from features.roles.application.usecases.getByColumn_usecase import GetByColumnUseCase
from features.roles.application.usecases.getById_usecase import GetByIdUseCase
from features.roles.application.usecases.list_usecase import listUseCase

from features.roles.infrastructure.role_repository import RoleRepository
from features.roles.application.contracts.create_contract import CreateContract
from features.roles.application.contracts.update_contract import UpdateContract
from features.roles.application.contracts.delete_contract import DeleteContract
from features.roles.application.contracts.getByColumn_contract import GetByColumnContract
from features.roles.application.contracts.getById_contract import GetByIdContract
from features.roles.application.contracts.response_contract import RoleResponseContract

class RoleServices:

    def __init__(self, repo : RoleRepository):
        self.create_usecase = CreateUseCase(repo)
        self.update_usecase = UpdateUseCase(repo)
        self.delete_usecase = DeleteUseCase(repo)
        self.list_usecase = listUseCase(repo)
        self.getById_usecase = GetByIdUseCase(repo)
        self.getByColumn_usecase = GetByColumnUseCase(repo)

    def createRole(self, contract : CreateContract)->RoleResponseContract:
        return self.create_usecase.execute(contract)
    
    def updateRole(self, contract : UpdateContract)->RoleResponseContract:
        return self.update_usecase.execute(contract)
    
    def deleteRole(self, contract : DeleteContract)->bool:
        return self.delete_usecase.execute(contract)
    
    def getByColumn(self, contract : GetByColumnContract)->RoleResponseContract:
        return self.getByColumn_usecase.execute(contract)
    
    def getById(self, contract : GetByIdContract)->RoleResponseContract:
        return self.getById_usecase.execute(contract)
    
    def allRoles(self)->list[RoleResponseContract]:
        return self.list_usecase.execute()