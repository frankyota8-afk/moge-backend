from dataclasses import dataclass
from typing import Optional
from features.rooms.application.contracts.response_contract import BuildingContract

@dataclass
class RoomGetByColumnContract:

    id:Optional[int]
    room_id:Optional[str]
    room_no:Optional[str] 
    room_name:Optional[str]
    building_id:Optional[str]