from features.stypes.infrastructure.stype_repository import StypeRepository
from features.stypes.application.contracts.getById_contract import GetByIdContract
from features.stypes.application.contracts.response_contract import StypeResponseContract

from features.stypes.domain.stype_entity import StypeEntity

class GetByIdUseCase:
    
    def __init__(self ,repo : StypeRepository):
        self.repo = repo

    def execute(self, contract : GetByIdContract)->StypeResponseContract:

        entity = StypeEntity(
            id=contract.id
        )

        entity = self.repo.getById(entity.id)

        return StypeResponseContract(
            id=entity.id,
            stype_id=entity.stype_id,
            stype_name=entity.stype_name
        )
