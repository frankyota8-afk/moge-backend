from dataclasses import dataclass

@dataclass
class RoomUpdateContract:

    id:int
    room_id:str
    room_no:str
    room_name:str
    building_id:int