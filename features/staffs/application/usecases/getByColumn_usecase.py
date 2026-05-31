from features.staffs.application.contracts.request_contracts import StaffGetByColumnContract
from features.staffs.domain.staff_entity import StaffEntity
from features.staffs.application.helpers.helper import contractToEntity
from features.staffs.infrastructure.staff_repository import StaffRepository
from features.staffs.domain.exceptions import CreateStaffUseCaseException, StaffAlreadyExistedException
from features.staffs.infrastructure.staff_mapper import StaffMapper
from features.staffs.models import Staff
from features.staffs.application.contracts.response_contract import StaffResponseContract


class GetByColumnUseCase:

    def execute(contract : StaffGetByColumnContract)->list[StaffResponseContract]:
        entity = contractToEntity(contract)    
        staffs = StaffRepository.getByColumn(entity)        
        return [
            StaffMapper.toContract(staff)
            for staff in staffs
        ]


        


