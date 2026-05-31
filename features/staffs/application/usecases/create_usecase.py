from features.staffs.application.contracts.request_contracts import StaffCreateContract
from features.staffs.domain.staff_entity import StaffEntity
from features.staffs.application.helpers.helper import contractToEntity
from features.staffs.infrastructure.staff_repository import StaffRepository
from features.staffs.domain.exceptions import CreateStaffUseCaseException, StaffAlreadyExistedException
from features.staffs.infrastructure.staff_mapper import StaffMapper
from features.staffs.models import Staff
from features.staffs.application.contracts.response_contract import StaffResponseContract


class CreateStaffUseCase:

    def generateId()->str:
        last_id = Staff.objects.order_by("-staff_id").values_list("staff_id", flat=True).first()
        if last_id:
            number = int(last_id.split("-")[1])+1
        else:
            number = 1

        return f"S-{number:03d}" 

    def execute(contract : StaffCreateContract)->StaffResponseContract:
        entity = contractToEntity(contract)
        if StaffRepository.getByEmail(entity.staff_email):
            raise StaffAlreadyExistedException("Staff already exist")
        else:
            entity.staff_id = CreateStaffUseCase.generateId()
            
        staff = StaffRepository.create(entity)

        if not staff:
            raise CreateStaffUseCaseException("Falied to create Staff")
        
        return StaffMapper.toContract(staff)


        


