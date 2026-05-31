from dataclasses import dataclass
from typing import Optional

@dataclass(kw_only=True)
class StaffCreateContract:
    staff_name:Optional[str]=None
    staff_email:Optional[str]=None
    staff_address:Optional[str]=None
    staff_ph_number:Optional[str]=None
    staff_gender:Optional[str]=None

    department_id:Optional[int]=None
    role_id:Optional[int]=None
    rank_id:Optional[int]=None
    stype_id:Optional[int]=None

@dataclass
class StaffUpdateContract:
    id:Optional[int]
    staff_id:Optional[str]
    staff_name:Optional[str]
    staff_email:Optional[str]
    staff_address:Optional[str]
    staff_ph_number:Optional[str]
    staff_gender:Optional[str]

    department_id:Optional[int]
    role_id:Optional[int]
    rank_id:Optional[int]
    stype_id:Optional[int]

@dataclass
class StaffDeleteContract:
    id:int

@dataclass
class StaffGetByIdContract:
    id:int



@dataclass(kw_only=True)
class StaffGetByColumnContract:
    staff_id:Optional[str]=None
    staff_name:Optional[str]=None
    staff_email:Optional[str]=None

    department_id:Optional[int]=None
    role_id:Optional[int]=None
    rank_id:Optional[int]=None
    stype_id:Optional[int]=None