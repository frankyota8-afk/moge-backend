from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from features.departments.domain.department_entity import DepartmentEntity
from features.roles.domain.role_entity import RoleEntity
from features.ranks.domain.rank_entity import RankEntity
from features.stypes.domain.stype_entity import StypeEntity

@dataclass(kw_only=True)
class StaffEntity:
    id:Optional[int] = None
    staff_id:Optional[str] = None
    staff_name:Optional[str] = None
    staff_email:Optional[str] = None
    staff_address:Optional[str] = None
    staff_ph_number:Optional[str] = None
    staff_gender:Optional[str] = None
    department_id:Optional[int] = None
    role_id:Optional[int] = None
    rank_id:Optional[int] = None
    stype_id:Optional[int] = None

    department:Optional[DepartmentEntity] = None
    role:Optional[RoleEntity] = None
    rank:Optional[RankEntity] = None
    stype:Optional[StypeEntity] = None

    created_at:Optional[datetime] = None
    updated_at:Optional[datetime] = None