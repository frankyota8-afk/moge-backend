from features.staffs.domain.staff_entity import StaffEntity
from dataclasses import asdict
from features.staffs.models import Staff
from features.staffs.application.contracts.response_contract import StaffResponseContract

class StaffMapper:

    def toEntity(model : Staff)->StaffEntity:
        return StaffEntity(
            id=model.id,
            staff_id=model.staff_id,
            staff_name=model.staff_name,
            staff_email=model.staff_email,
            staff_address=model.staff_address,
            staff_ph_number=model.staff_ph_number,
            staff_gender=model.staff_gender,
            department_id=model.department_id,
            role_id=model.role_id,
            rank_id=model.rank_id,
            stype_id=model.stype_id,
            department=model.department,
            role=model.role,
            rank=model.rank,
            stype=model.stype,
        )
    
    def toModel(entity: StaffEntity)->dict:
        return {
            "id":entity.id,
            "staff_id":entity.staff_id,
            "staff_name":entity.staff_name,
            "staff_email":entity.staff_email,
            "staff_address":entity.staff_address,
            "staff_ph_number":entity.staff_ph_number,
            "staff_gender":entity.staff_gender,
            "department_id":entity.department_id,
            "role_id":entity.role_id,
            "rank_id":entity.rank_id,
            "stype_id":entity.stype_id,
        }
    
    @staticmethod
    def toContract(entity: StaffEntity) -> StaffResponseContract:
        return StaffResponseContract(
            id=entity.id,
            staff_id=entity.staff_id,
            staff_name=entity.staff_name,
            staff_email=entity.staff_email,
            staff_address=entity.staff_address,
            staff_ph_number=entity.staff_ph_number,
            staff_gender=entity.staff_gender,
            department_id=entity.department_id,
            role_id=entity.role_id,
            rank_id=entity.rank_id,
            stype_id=entity.stype_id,
            department=entity.department,
            role=entity.role,
            rank=entity.rank,
            stype=entity.stype,
        )

