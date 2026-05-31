from features.rooms.infrastructure.room_repository import RoomRepository
from features.rooms.application.contracts.delete_contract import RoomDeleteContract
from features.rooms.application.contracts.response_contract import RoomResponseContract

from features.rooms.domain.room_entity import RoomEntity

class DeleteUseCase:
    
    def __init__(self ,repo : RoomRepository):
        self.repo = repo

    def execute(self, contract : RoomDeleteContract)->RoomResponseContract:

        entity = RoomEntity(
            id=contract.id
        )
        
        return self.repo.delete(entity)
