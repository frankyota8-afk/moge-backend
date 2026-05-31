from authentication.application.usecases import AllUserUseCase, DeleteUserUseCase, GetUserByIdUserCase
from authentication.infrastructure.user_repository import UserRepository

class UserService:

    def __init__(self, repo : UserRepository):
        self.all_user_usecase = AllUserUseCase(repo)
        self.delete_user_usecase = DeleteUserUseCase(repo)
        self.get_user_byId_usecase = GetUserByIdUserCase(repo)
        

    def all(self):
        return self.all_user_usecase.execute()
    
    def getUserById(self, id:int):
        return self.get_user_byId_usecase.execute(id)
    
    def delete(self, id:int):
        return self.delete_user_usecase.execute(id)