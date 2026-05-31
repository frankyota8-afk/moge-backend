from features.staffs.application.contracts.request_contracts import StaffGetByIdContract
from features.staffs.domain.staff_entity import StaffEntity
from features.staffs.application.helpers.helper import contractToEntity
from features.staffs.infrastructure.staff_repository import StaffRepository
from features.staffs.domain.exceptions import CreateStaffUseCaseException, StaffAlreadyExistedException
from features.staffs.infrastructure.staff_mapper import StaffMapper
from features.staffs.models import Staff
from features.staffs.application.contracts.response_contract import StaffResponseContract


class GetByIdUseCase:

    def execute(contract : StaffGetByIdContract)->StaffResponseContract:
        entity = contractToEntity(contract)    
        staffs = StaffRepository.getById(entity)        
        return StaffMapper.toContract(staffs)


        


