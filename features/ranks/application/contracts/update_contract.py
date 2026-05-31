from dataclasses import dataclass
from typing import Optional

@dataclass
class UpdateContract:

    id:int
    rank_id:str
    rank_name:str