from dataclasses import dataclass
from typing import Optional

@dataclass
class GetByColumnContract:

    id:Optional[int]
    rank_id:Optional[str]
    rank_name:Optional[str]