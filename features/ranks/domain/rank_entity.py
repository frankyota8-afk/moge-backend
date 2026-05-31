from dataclasses import dataclass
from typing import Optional

@dataclass(kw_only=True)
class RankEntity:

    id:Optional[int]=None
    rank_id:Optional[str]=None
    rank_name:str=None