from features.ranks.infrastructure.rank_repository import RankRepository
from features.ranks.application.contracts.getById_contract import GetByIdContract
from features.ranks.application.contracts.response_contract import RankResponseContract

from features.ranks.domain.rank_entity import RankEntity

class GetByIdUseCase:
    
    def __init__(self ,repo : RankRepository):
        self.repo = repo

    def execute(self, contract : GetByIdContract)->RankResponseContract:

        entity = RankEntity(
            id=contract.id
        )

        entity = self.repo.getById(entity.id)

        return RankResponseContract(
            id=entity.id,
            rank_id=entity.rank_id,
            rank_name=entity.rank_name
        )
