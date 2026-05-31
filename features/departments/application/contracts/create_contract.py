from dataclasses import dataclass

@dataclass
class DepartmentCreateContract:
    department_name:str
    room_id:int

