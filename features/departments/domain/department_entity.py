from dataclasses import dataclass
from typing import Optional
from features.rooms.domain.room_entity import RoomEntity

@dataclass(kw_only=True)
class DepartmentEntity:
    id: Optional[int] = None
    department_id: str = None
    department_name: str = None
    room_id: Optional[int] = None
    room:Optional[RoomEntity] = None
