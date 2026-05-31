from dataclasses import dataclass
from typing import Optional

@dataclass
class GetByColumnContract:

    id:Optional[int]
    stype_id:Optional[str]
    stype_name:Optional[str] 