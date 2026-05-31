from features.staffs.application.contracts.request_contracts import StaffUpdateContract
from features.staffs.domain.staff_entity import StaffEntity
from features.staffs.application.helpers.helper import contractToEntity
from features.staffs.infrastructure.staff_repository import StaffRepository
from features.staffs.domain.exceptions import UpdateStaffUseCaseException
from features.staffs.infrastructure.staff_mapper import StaffMapper
from features.staffs.models import Staff
from features.staffs.application.contracts.response_contract import StaffResponseContract


class UpdateStaffUseCase:

    def execute(contract : StaffUpdateContract)->StaffResponseContract:
        entity = contractToEntity(contract)
            
        staff = StaffRepository.update(entity)

        if not staff:
            raise UpdateStaffUseCaseException("Falied to update Staff")
        
        return StaffMapper.toContract(staff)


        


