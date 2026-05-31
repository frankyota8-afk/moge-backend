from features.rooms.infrastructure.room_repository import RoomRepository
from features.rooms.application.contracts.create_contract import RoomCreateContract
from features.rooms.application.contracts.response_contract import RoomResponseContract
from features.rooms.infrastructure.room_mapper import RoomMapper

from features.rooms.domain.room_entity import RoomEntity
from features.rooms.domain.exceptions import RoomAlreadyExistedException

class CreateUseCase:
    
    def __init__(self ,repo : RoomRepository):
        self.repo = repo

    def execute(self, contract : RoomCreateContract)->RoomResponseContract:

        create_entity = RoomEntity(
            room_no=contract.room_no,
            room_name=contract.room_name,
            building_id=contract.building_id,
        )
        if self.repo.existByName(create_entity):
            raise RoomAlreadyExistedException("Room name has been already existed!")
        else:
            create_entity.room_id = self.repo.generateId("room_id","ROOM")
            
        response_entity = self.repo.create(create_entity)

        return RoomMapper.toContract(response_entity)
