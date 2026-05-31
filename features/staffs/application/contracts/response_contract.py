from dataclasses import dataclass
from typing import Optional
from features.departments.application.contracts.response_contract import DepartmentResponseContract
from features.roles.application.contracts.response_contract import RoleResponseContract
from features.ranks.application.contracts.response_contract import RankResponseContract
from features.stypes.application.contracts.response_contract import StypeResponseContract

@dataclass(kw_only=True)
class StaffResponseContract:
    id:Optional[int]=None
    staff_id:Optional[str]=None
    staff_name:Optional[str]=None
    staff_email:Optional[str]=None
    staff_address:Optional[str]=None
    staff_ph_number:Optional[str]=None
    staff_gender:Optional[str]=None

    department_id:Optional[int]=None
    role_id:Optional[int]=None
    rank_id:Optional[int]=None
    stype_id:Optional[int]=None

    department:Optional[DepartmentResponseContract] = None
    role:Optional[RoleResponseContract] = None
    rank:Optional[RankResponseContract] = None
    stype:Optional[StypeResponseContract] = None

@dataclass
class ApiResponse:
    data : list[StaffResponseContract]
    message : Optional[str]