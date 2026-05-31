from dataclasses import dataclass

@dataclass
class RoleResponseContract:
    id:int
    role_id:str
    role_name:str