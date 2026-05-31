from typing import Optional
from dataclasses import dataclass

@dataclass(kw_only=True)
class BuildingEntity:
    id:Optional[int]=None
    building_id:Optional[str]=None
    building_name:Optional[str]=None

@dataclass(kw_only=True)
class RoomEntity:
    id:Optional[int]=None
    room_id:Optional[str]=None
    room_no:Optional[str]=None
    room_name:Optional[str]=None
    building_id:Optional[str]=None
    building:Optional[BuildingEntity]=None
