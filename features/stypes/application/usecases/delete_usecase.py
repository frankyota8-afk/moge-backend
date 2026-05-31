from features.stypes.infrastructure.stype_repository import StypeRepository
from features.stypes.application.contracts.delete_contract import DeleteContract
from features.stypes.application.contracts.response_contract import StypeResponseContract

from features.stypes.domain.stype_entity import StypeEntity

class DeleteUseCase:
    
    def __init__(self ,repo : StypeRepository):
        self.repo = repo

    def execute(self, contract : DeleteContract)->StypeResponseContract:

        entity = StypeEntity(
            id=contract.id
        )
        
        return self.repo.delete(entity)
