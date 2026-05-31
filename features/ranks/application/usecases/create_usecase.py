from features.ranks.infrastructure.rank_repository import RankRepository
from features.ranks.application.contracts.create_contract import CreateContract
from features.ranks.application.contracts.response_contract import RankResponseContract

from features.ranks.domain.rank_entity import RankEntity
from features.ranks.domain.exceptions import RankAlreadyExistException

class CreateUseCase:
    
    def __init__(self ,repo : RankRepository):
        self.repo = repo

    def execute(self, contract : CreateContract)->RankResponseContract:

        create_entity = RankEntity(
            rank_name=contract.rank_name
        )
        if self.repo.existByName(create_entity):
            raise RankAlreadyExistException("Rank name has been already existed!")
        else:
            create_entity.rank_id = self.repo.generateId("rank_id","RANK")
            
        response_entity = self.repo.create(create_entity)

        return RankResponseContract(
            id=response_entity.id,
            rank_id=response_entity.rank_id,
            rank_name=response_entity.rank_name
        )
