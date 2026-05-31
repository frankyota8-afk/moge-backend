from dataclasses import dataclass
from typing import Optional

@dataclass
class BuildingContract:
    id:int
    building_id:str
    building_name:str

@dataclass
class RoomResponseContract:
    id:int
    room_id: str
    room_no:str
    room_name:str
    building_id:int
    building:BuildingContract