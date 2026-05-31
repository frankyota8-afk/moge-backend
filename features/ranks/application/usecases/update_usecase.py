from features.ranks.application.contracts.update_contract import UpdateContract
from features.ranks.application.contracts.response_contract import RankResponseContract
from features.ranks.infrastructure.rank_repository import RankRepository
from features.ranks.domain.rank_entity import RankEntity

class UpdateUseCase:

    def __init__(self, repo : RankRepository):
        self.repo = repo

    def execute(self, contract : UpdateContract)->RankResponseContract:
        entity = RankEntity(
            id=contract.id,
            rank_id=contract.rank_id,
            rank_name=contract.rank_name
        )

        entity = self.repo.update(entity)

        return RankResponseContract(
            id=entity.id,
            rank_id=entity.rank_id,
            rank_name=entity.rank_name
        )
        