from features.rooms.domain.room_entity import RoomEntity
from features.rooms.models import Room
from features.rooms.application.contracts.response_contract import RoomResponseContract


class RoomMapper:

    def toEntity(room : Room)->RoomEntity:
        
        return RoomEntity(
            id=room.id,
            room_id=room.room_id,
            room_no = room.room_no,
            room_name=room.room_name,
            building_id=room.building_id,
            building=room.building,
        )
    
    def toModel(entity : RoomEntity)->dict:
        return {
            "room_id" : entity.room_id,
            "room_no" : entity.room_no,
            "room_name" : entity.room_name,
            "building_id" : entity.building_id,
        }
    
    @staticmethod
    def toContract(entity: RoomEntity)->RoomResponseContract:
        return RoomResponseContract(
            id=entity.id,
            room_id=entity.room_id,
            room_no=entity.room_no,
            room_name=entity.room_name,
            building_id=entity.building_id,
            building=entity.building
        )