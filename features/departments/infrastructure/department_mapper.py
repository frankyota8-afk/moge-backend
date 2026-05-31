# features/departments/infrastructure/department_mapper.py
from features.departments.domain.department_entity import DepartmentEntity
from features.departments.models import Department
from features.rooms.infrastructure.room_mapper import RoomMapper

class DepartmentMapper:

    @staticmethod
    def toEntity(data: Department) -> DepartmentEntity:
        return DepartmentEntity(
            id=data.id,
            department_id=data.department_id,
            department_name=data.department_name,
            room_id=data.room.id if data.room else None,
            room=RoomMapper.toEntity(data.room) if data.room else None
        )

    @staticmethod
    def toModel(entity: DepartmentEntity) -> dict:
        return {
            "department_id": entity.department_id,
            "department_name": entity.department_name,
            "room_id": entity.room_id
        }
