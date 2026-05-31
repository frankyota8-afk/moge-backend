from dataclasses import dataclass
from typing import Optional

@dataclass
class GetByColumnContract:

    id:Optional[int] = None
    role_id:Optional[str] = None
    role_name:Optional[str] = None