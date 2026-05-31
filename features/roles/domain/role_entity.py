from dataclasses import dataclass
from typing import Optional

@dataclass(kw_only=True)
class RoleEntity:
    id:Optional[int] = None
    role_id:Optional[str] = None
    role_name:str = None
    