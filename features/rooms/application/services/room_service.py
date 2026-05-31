from features.rooms.application.usecases.create_usecase import CreateUseCase
from features.rooms.application.usecases.update_usecase import UpdateUseCase
from features.rooms.application.usecases.delete_usecase import DeleteUseCase
from features.rooms.application.usecases.getByColumn_usecase import GetByColumnUseCase
from features.rooms.application.usecases.getById_usecase import GetByIdUseCase
from features.rooms.application.usecases.list_usecase import listUseCase

from features.rooms.infrastructure.room_repository import RoomRepository
from features.rooms.application.contracts.create_contract import RoomCreateContract
from features.rooms.application.contracts.update_contract import RoomUpdateContract
from features.rooms.application.contracts.delete_contract import RoomDeleteContract
from features.rooms.application.contracts.getByColumn_contract import RoomGetByColumnContract
from features.rooms.application.contracts.getById_contract import GetRoomByIdContract
from features.rooms.application.contracts.response_contract import RoomResponseContract

class RoomService:

    def __init__(self, repo : RoomRepository):
        self.create_usecase = CreateUseCase(repo)
        self.update_usecase = UpdateUseCase(repo)
        self.delete_usecase = DeleteUseCase(repo)
        self.list_usecase = listUseCase(repo)
        self.getById_usecase = GetByIdUseCase(repo)
        self.getByColumn_usecase = GetByColumnUseCase(repo)

    def createRoom(self, contract : RoomCreateContract)->RoomResponseContract:
        return self.create_usecase.execute(contract)
    
    def updateRoom(self, contract : RoomUpdateContract)->RoomResponseContract:
        return self.update_usecase.execute(contract)
    
    def deleteRoom(self, contract : RoomDeleteContract)->bool:
        return self.delete_usecase.execute(contract)
    
    def getByColumn(self, contract : RoomGetByColumnContract)->RoomResponseContract:
        return self.getByColumn_usecase.execute(contract)
    
    def getById(self, contract : GetRoomByIdContract)->RoomResponseContract:
        return self.getById_usecase.execute(contract)
    
    def allRooms(self)->list[RoomResponseContract]:
        return self.list_usecase.execute()