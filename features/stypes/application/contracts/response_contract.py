from dataclasses import dataclass
from typing import Optional

@dataclass
class StypeResponseContract:
    id:int
    stype_id: str
    stype_name:str