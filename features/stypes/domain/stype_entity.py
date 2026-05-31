from typing import Optional
from dataclasses import dataclass

@dataclass(kw_only=True)
class StypeEntity:
    id:Optional[int] =None
    stype_id:Optional[str] =None
    stype_name:Optional[str] =None
