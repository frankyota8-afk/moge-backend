from features.rooms.infrastructure.room_repository import RoomRepository
from features.rooms.application.contracts.getById_contract import GetRoomByIdContract
from features.rooms.application.contracts.response_contract import RoomResponseContract
from features.rooms.infrastructure.room_mapper import RoomMapper

from features.rooms.domain.room_entity import RoomEntity

class GetByIdUseCase:
    
    def __init__(self ,repo : RoomRepository):
        self.repo = repo

    def execute(self, contract : GetRoomByIdContract)->RoomResponseContract:

        entity = RoomEntity(
            id=contract.id
        )

        entity = self.repo.getById(entity.id)

        return RoomMapper.toContract(entity)
