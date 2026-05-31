from features.ranks.infrastructure.rank_repository import RankRepository
from features.ranks.application.contracts.getByColumn_contract import GetByColumnContract
from features.ranks.application.contracts.response_contract import RankResponseContract

from features.ranks.domain.rank_entity import RankEntity

class GetByColumnUseCase:
    
    def __init__(self ,repo : RankRepository):
        self.repo = repo

    def execute(self, contract : GetByColumnContract)->RankResponseContract:

        entity = RankEntity(
            id=contract.id,
            rank_id=contract.rank_id,
            rank_name=contract.rank_name
        )

        entities = self.repo.getAllByColumns(entity)

        return [
            RankResponseContract(
                id=entity.id,
                rank_id=entity.rank_id,
                rank_name=entity.rank_name
            )
            for entity in entities
        ]
