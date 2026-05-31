from features.roles.infrastructure.role_repository import RoleRepository
from features.roles.application.contracts.getByColumn_contract import GetByColumnContract
from features.roles.application.contracts.response_contract import RoleResponseContract

from features.roles.domain.role_entity import RoleEntity

class GetByColumnUseCase:
    
    def __init__(self ,repo : RoleRepository):
        self.repo = repo

    def execute(self, contract : GetByColumnContract)->RoleResponseContract:

        entity = RoleEntity(
            id=contract.id,
            role_id=contract.role_id,
            role_name=contract.role_name
        )

        entities = self.repo.getAllByColumns(entity)

        return [
            RoleResponseContract(
                id=entity.id,
                role_id=entity.role_id,
                role_name=entity.role_name
            )
            for entity in entities
        ]
