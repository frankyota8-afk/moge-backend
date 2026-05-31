from features.staffs.infrastructure.staff_repository import StaffRepository
from features.staffs.domain.staff_entity import StaffEntity
from features.staffs.domain.exceptions import StaffNotFoundException
from features.staffs.infrastructure.staff_mapper import StaffMapper
from features.staffs.application.contracts.response_contract import StaffResponseContract

class AllStaffUseCase:

    def execute()->list[StaffResponseContract]:
        
        staffs = StaffRepository.all()
        # if not staffs:
        #     raise StaffNotFoundException("No staff's data have been found")
        return [
            StaffMapper.toContract(staff)
            for staff in staffs
        ]
        
