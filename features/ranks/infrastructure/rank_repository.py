from features.shared.repositories.base_repository import BaseRepository
from features.ranks.domain.rank_entity import RankEntity

class RankRepository(BaseRepository):

    def all(self)->list[RankEntity]:
        return super().all()
    
    def getById(self, id)->RankEntity:
        return super().getById(id)
    
    def getAllByColumns(self, entity)->list[RankEntity]:
        return super().getAllByColumns(entity)

    def create(self, entity)->RankEntity:
        return super().create(entity)
    
    def update(self, entity)->RankEntity:
        return super().update(entity)