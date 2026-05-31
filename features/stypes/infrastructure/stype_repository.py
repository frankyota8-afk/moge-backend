from features.shared.repositories.base_repository import BaseRepository
from features.stypes.domain.stype_entity import StypeEntity
from features.stypes.models import Stype

class StypeRepository(BaseRepository):

    def create(self, entity: StypeEntity)->StypeEntity:
        return super().create(entity)
    
    def update(self, entity: StypeEntity)->StypeEntity:
        return super().update(entity)
    
    def all(self)->list[StypeEntity]:
        return super().all()
    
    def delete(self, entity):
        return super().delete(entity)
    
    def getAllByColumns(self, entity)->list[StypeEntity]:
        return super().getAllByColumns(entity)
    
    def getById(self, id)->StypeEntity:
        return super().getById(id)
