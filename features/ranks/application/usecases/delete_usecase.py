from features.ranks.infrastructure.rank_repository import RankRepository
from features.ranks.application.contracts.delete_contract import DeleteContract
from features.ranks.application.contracts.response_contract import RankResponseContract

from features.ranks.domain.rank_entity import RankEntity

class DeleteUseCase:
    
    def __init__(self ,repo : RankRepository):
        self.repo = repo

    def execute(self, contract : DeleteContract)->RankResponseContract:

        entity = RankEntity(
            id=contract.id
        )
        
        return self.repo.delete(entity)
