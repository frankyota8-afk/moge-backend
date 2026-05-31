from features.shared.repositories.base_repository import BaseRepository
from features.rooms.domain.room_entity import RoomEntity
from features.rooms.models import Room

class RoomRepository(BaseRepository):

    def create(self, entity: RoomEntity)->RoomEntity:
        return super().create(entity)
    
    def update(self, entity: RoomEntity)->RoomEntity:
        return super().update(entity)
    
    def all(self)->list[RoomEntity]:
        return super().all()
    
    def delete(self, entity):
        return super().delete(entity)
    
    def getAllByColumns(self, entity)->list[RoomEntity]:
        return super().getAllByColumns(entity)
    
    def getById(self, id)->RoomEntity:
        return super().getById(id)
