from features.stypes.application.usecases.create_usecase import CreateUseCase
from features.stypes.application.usecases.update_usecase import UpdateUseCase
from features.stypes.application.usecases.delete_usecase import DeleteUseCase
from features.stypes.application.usecases.getByColumn_usecase import GetByColumnUseCase
from features.stypes.application.usecases.getById_usecase import GetByIdUseCase
from features.stypes.application.usecases.list_usecase import listUseCase

from features.stypes.infrastructure.stype_repository import StypeRepository
from features.stypes.application.contracts.create_contract import CreateContract
from features.stypes.application.contracts.update_contract import UpdateContract
from features.stypes.application.contracts.delete_contract import DeleteContract
from features.stypes.application.contracts.getByColumn_contract import GetByColumnContract
from features.stypes.application.contracts.getById_contract import GetByIdContract
from features.stypes.application.contracts.response_contract import StypeResponseContract

class StypeService:

    def __init__(self, repo : StypeRepository):
        self.create_usecase = CreateUseCase(repo)
        self.update_usecase = UpdateUseCase(repo)
        self.delete_usecase = DeleteUseCase(repo)
        self.list_usecase = listUseCase(repo)
        self.getById_usecase = GetByIdUseCase(repo)
        self.getByColumn_usecase = GetByColumnUseCase(repo)

    def createStype(self, contract : CreateContract)->StypeResponseContract:
        return self.create_usecase.execute(contract)
    
    def updateStype(self, contract : UpdateContract)->StypeResponseContract:
        return self.update_usecase.execute(contract)
    
    def deleteStype(self, contract : DeleteContract)->bool:
        return self.delete_usecase.execute(contract)
    
    def getByColumn(self, contract : GetByColumnContract)->StypeResponseContract:
        return self.getByColumn_usecase.execute(contract)
    
    def getById(self, contract : GetByIdContract)->StypeResponseContract:
        return self.getById_usecase.execute(contract)
    
    def allStypes(self)->list[StypeResponseContract]:
        return self.list_usecase.execute()