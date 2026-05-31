from features.departments.domain.department_entity import DepartmentEntity

def contractToEntity(contract)->DepartmentEntity:
    return DepartmentEntity(
        id=contract.id if contract.id else None,
        department_id=contract.department_id if contract.department_id else None,
        department_name=contract.department_name if contract.department_name else None,
        room_id=contract.room_id if contract.room_id else None,
        room=contract.room if contract.room else None,
    )

def remove_noneValues(data : dict)->dict:
    return {k:v for k,v in data.items() if v is not None}
