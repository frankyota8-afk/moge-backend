from dataclasses import dataclass
from typing import Optional

@dataclass
class RoomCreateContract:
    room_no:str
    room_name:str
    building_id:int