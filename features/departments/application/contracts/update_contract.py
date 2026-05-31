from dataclasses import dataclass

@dataclass
class DepartmentUpdateContract:
    id:int
    department_id:str
    department_name:str
    room_id:int

