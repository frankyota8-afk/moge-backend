from dataclasses import dataclass
from datetime import datetime


@dataclass
class Match:
    page:str
    line:str
    text:str

@dataclass
class DeepSearchDocument:
    id:int
    filename:str
    department_name:str
    uploaded_at:str
    category:str
    file_url:str

    matches: list[Match]