from features.roles.infrastructure.role_repository import RoleRepository
from features.roles.application.contracts.delete_contract import DeleteContract
from features.roles.application.contracts.response_contract import RoleResponseContract

from features.roles.domain.role_entity import RoleEntity

class DeleteUseCase:
    
    def __init__(self ,repo : RoleRepository):
        self.repo = repo

    def execute(self, contract : DeleteContract)->RoleResponseContract:

        
        entity = RoleEntity(
            id=contract.id
        )
        
        return self.repo.delete(entity)
