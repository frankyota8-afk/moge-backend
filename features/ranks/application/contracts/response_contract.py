from dataclasses import dataclass
from typing import Optional

@dataclass(kw_only=True)
class RankResponseContract:

    id:Optional[int] = None
    rank_id:str
    rank_name:str