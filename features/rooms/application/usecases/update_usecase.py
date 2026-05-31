from features.rooms.application.contracts.update_contract import RoomUpdateContract
from features.rooms.application.contracts.response_contract import RoomResponseContract
from features.rooms.infrastructure.room_repository import RoomRepository
from features.rooms.domain.room_entity import RoomEntity
from features.rooms.infrastructure.room_mapper import RoomMapper

class UpdateUseCase:

    def __init__(self, repo : RoomRepository):
        self.repo = repo

    def execute(self, contract : RoomUpdateContract)->RoomResponseContract:
        entity = RoomEntity(
            id=contract.id,
            room_id=contract.room_id,
            room_no=contract.room_no,
            room_name=contract.room_name,
            building_id=contract.building_id,
        )

        entity = self.repo.update(entity)

        return RoomMapper.toContract(entity)
        