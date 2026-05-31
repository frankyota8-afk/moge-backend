from features.staffs.application.contracts.request_contracts import StaffDeleteContract
from features.staffs.domain.staff_entity import StaffEntity
from features.staffs.application.helpers.helper import contractToEntity
from features.staffs.infrastructure.staff_repository import StaffRepository
from features.staffs.domain.exceptions import UpdateStaffUseCaseException
from features.staffs.infrastructure.staff_mapper import StaffMapper
from features.staffs.models import Staff


class DeleteStaffUseCase:

    def execute(contract : StaffDeleteContract):
        entity = contractToEntity(contract)
            
        res = StaffRepository.delete(entity)

        if not res:
            raise UpdateStaffUseCaseException("Falied to delete Staff")
        
        return "Deleted Successfully!"


        


