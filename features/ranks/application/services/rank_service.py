from features.ranks.application.usecases.create_usecase import CreateUseCase
from features.ranks.application.usecases.update_usecase import UpdateUseCase
from features.ranks.application.usecases.delete_usecase import DeleteUseCase
from features.ranks.application.usecases.getByColumn_usecase import GetByColumnUseCase
from features.ranks.application.usecases.getById_usecase import GetByIdUseCase
from features.ranks.application.usecases.list_usecase import listUseCase

from features.ranks.infrastructure.rank_repository import RankRepository
from features.ranks.application.contracts.create_contract import CreateContract
from features.ranks.application.contracts.update_contract import UpdateContract
from features.ranks.application.contracts.delete_contract import DeleteContract
from features.ranks.application.contracts.getByColumn_contract import GetByColumnContract
from features.ranks.application.contracts.getById_contract import GetByIdContract
from features.ranks.application.contracts.response_contract import RankResponseContract

class RankService:

    def __init__(self, repo : RankRepository):
        self.create_usecase = CreateUseCase(repo)
        self.update_usecase = UpdateUseCase(repo)
        self.delete_usecase = DeleteUseCase(repo)
        self.list_usecase = listUseCase(repo)
        self.getById_usecase = GetByIdUseCase(repo)
        self.getByColumn_usecase = GetByColumnUseCase(repo)

    def createRank(self, contract : CreateContract)->RankResponseContract:
        return self.create_usecase.execute(contract)
    
    def updateRank(self, contract : UpdateContract)->RankResponseContract:
        return self.update_usecase.execute(contract)
    
    def deleteRank(self, contract : DeleteContract)->bool:
        return self.delete_usecase.execute(contract)
    
    def getByColumn(self, contract : GetByColumnContract)->RankResponseContract:
        return self.getByColumn_usecase.execute(contract)
    
    def getById(self, contract : GetByIdContract)->RankResponseContract:
        return self.getById_usecase.execute(contract)
    
    def allranks(self)->list[RankResponseContract]:
        return self.list_usecase.execute()