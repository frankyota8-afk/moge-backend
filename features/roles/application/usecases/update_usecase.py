from features.roles.application.contracts.update_contract import UpdateContract
from features.roles.application.contracts.response_contract import RoleResponseContract
from features.roles.infrastructure.role_repository import RoleRepository
from features.roles.domain.role_entity import RoleEntity

class UpdateUseCase:

    def __init__(self, repo : RoleRepository):
        self.repo = repo

    def execute(self, contract : UpdateContract)->RoleResponseContract:
        entity = RoleEntity(
            id=contract.id,
            role_id=contract.role_id,
            role_name=contract.role_name
        )

        entity = self.repo.update(entity)

        return RoleResponseContract(
            id=entity.id,
            role_id=entity.role_id,
            role_name=entity.role_name
        )
        