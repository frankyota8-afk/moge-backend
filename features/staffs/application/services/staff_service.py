from features.staffs.application.usecases.all_usecase import AllStaffUseCase
from features.staffs.application.usecases.create_usecase import CreateStaffUseCase
from features.staffs.application.usecases.update_usecase import UpdateStaffUseCase
from features.staffs.application.usecases.delete_usecase import DeleteStaffUseCase
from features.staffs.application.usecases.getByColumn_usecase import GetByColumnUseCase
from features.staffs.application.usecases.getById_usecase import GetByIdUseCase
from features.staffs.application.contracts.request_contracts import StaffCreateContract, StaffGetByIdContract, StaffUpdateContract, StaffDeleteContract, StaffGetByColumnContract
from features.staffs.domain.staff_entity import StaffEntity
from features.staffs.application.contracts.response_contract import StaffResponseContract


class StaffService:
  
    def createStaff(contract : StaffCreateContract):
        return CreateStaffUseCase.execute(contract), "Created successfully!"
    
    def updateStaff(contract : StaffUpdateContract):
        return UpdateStaffUseCase.execute(contract), "Updated successfully!"
    
    def deleteStaff(contract : StaffDeleteContract):
        return DeleteStaffUseCase.execute(contract)
    
    def allStaffs()->list[StaffResponseContract]:
        return AllStaffUseCase.execute()
    
    def getStaffsByColumn(contract : StaffGetByColumnContract)->list[StaffResponseContract]:
        return GetByColumnUseCase.execute(contract)

    def getStaffsById(contract : StaffGetByIdContract)->StaffResponseContract:
        return GetByIdUseCase.execute(contract)
    
    
