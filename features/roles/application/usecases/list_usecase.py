from features.roles.infrastructure.role_repository import RoleRepository
from features.roles.application.contracts.response_contract import RoleResponseContract

from features.roles.domain.role_entity import RoleEntity

class listUseCase:
    
    def __init__(self ,repo : RoleRepository):
        self.repo = repo

    def execute(self)->list[RoleResponseContract]:
        entities = self.repo.all()

        return [
            RoleResponseContract(
                id=entity.id,
                role_id=entity.role_id,
                role_name=entity.role_name
            )
            for entity in entities
        ]
