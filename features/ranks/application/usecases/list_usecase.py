from features.ranks.infrastructure.rank_repository import RankRepository
from features.ranks.application.contracts.response_contract import RankResponseContract

from features.ranks.domain.rank_entity import RankEntity

class listUseCase:
    
    def __init__(self ,repo : RankRepository):
        self.repo = repo

    def execute(self)->list[RankResponseContract]:
        entities = self.repo.all()

        return [
            RankResponseContract(
                id=entity.id,
                rank_id=entity.rank_id,
                rank_name=entity.rank_name
            )
            for entity in entities
        ]
