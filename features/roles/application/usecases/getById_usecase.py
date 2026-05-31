from features.roles.infrastructure.role_repository import RoleRepository
from features.roles.application.contracts.getById_contract import GetByIdContract
from features.roles.application.contracts.response_contract import RoleResponseContract

from features.roles.domain.role_entity import RoleEntity

class GetByIdUseCase:
    
    def __init__(self ,repo : RoleRepository):
        self.repo = repo

    def execute(self, contract : GetByIdContract)->RoleResponseContract:

        entity = RoleEntity(
            id=contract.id
        )

        entity = self.repo.getById(entity.id)

        return RoleResponseContract(
            id=entity.id,
            role_id=entity.role_id,
            role_name=entity.role_name
        )
