from dataclasses import dataclass
from typing import Optional

@dataclass
class GetByColumnContract:
    id:Optional[int]
    department_id:Optional[int]
    department_name:Optional[int]
    room_id:Optional[int]