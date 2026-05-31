from features.stypes.infrastructure.stype_repository import StypeRepository
from features.stypes.application.contracts.getByColumn_contract import GetByColumnContract
from features.stypes.application.contracts.response_contract import StypeResponseContract

from features.stypes.domain.stype_entity import StypeEntity

class GetByColumnUseCase:
    
    def __init__(self ,repo : StypeRepository):
        self.repo = repo

    def execute(self, contract : GetByColumnContract)->StypeResponseContract:

        entity = StypeEntity(
            id=contract.id,
            stype_id=contract.stype_id,
            stype_name=contract.stype_name
        )

        entities = self.repo.getAllByColumns(entity)

        return [
            StypeResponseContract(
                id=entity.id,
                stype_id=entity.stype_id,
                stype_name=entity.stype_name
            )
            for entity in entities
        ]
