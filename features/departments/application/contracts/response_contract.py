from dataclasses import dataclass
from typing import Optional
from features.rooms.application.contracts.response_contract import RoomResponseContract

@dataclass
class DepartmentResponseContract:

    id:Optional[int] = None
    department_id:Optional[str] = None
    department_name:Optional[str] = None
    room_id:Optional[int] = None
    room:Optional[RoomResponseContract] = None
    message:Optional[str] = None