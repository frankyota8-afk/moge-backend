from features.roles.infrastructure.role_repository import RoleRepository
from features.roles.application.contracts.create_contract import CreateContract
from features.roles.application.contracts.response_contract import RoleResponseContract

from features.roles.domain.role_entity import RoleEntity
from features.roles.domain.exceptions import RoleAlreadyExistedException

class CreateUseCase:
    
    def __init__(self ,repo : RoleRepository):
        self.repo = repo

    def execute(self, contract : CreateContract)->RoleResponseContract:

        create_entity = RoleEntity(
            role_name=contract.role_name
        )
        if self.repo.existByName(create_entity):
            raise RoleAlreadyExistedException("Role name has been already existed!")
        else:
            create_entity.role_id = self.repo.generateId("role_id","ROLE")
            
        response_entity = self.repo.create(create_entity)

        return RoleResponseContract(
            id=response_entity.id,
            role_id=response_entity.role_id,
            role_name=response_entity.role_name
        )
