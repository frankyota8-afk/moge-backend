from features.rooms.infrastructure.room_repository import RoomRepository
from features.rooms.application.contracts.getByColumn_contract import RoomGetByColumnContract
from features.rooms.application.contracts.response_contract import RoomResponseContract
from features.rooms.infrastructure.room_mapper import RoomMapper

from features.rooms.domain.room_entity import RoomEntity

class GetByColumnUseCase:
    
    def __init__(self ,repo : RoomRepository):
        self.repo = repo

    def execute(self, contract : RoomGetByColumnContract)->RoomResponseContract:

        entity = RoomEntity(
            id=contract.id,
            room_id=contract.room_id,
            room_name=contract.room_name,
            building_id=contract.building_id
        )

        entities = self.repo.getAllByColumns(entity)

        return [
            RoomMapper.toContract(entity)
            for entity in entities
        ]
