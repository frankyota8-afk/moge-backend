from features.stypes.infrastructure.stype_repository import StypeRepository
from features.stypes.application.contracts.response_contract import StypeResponseContract

from features.stypes.domain.stype_entity import StypeEntity

class listUseCase:
    
    def __init__(self ,repo : StypeRepository):
        self.repo = repo

    def execute(self)->list[StypeResponseContract]:
        entities = self.repo.all()

        return [
            StypeResponseContract(
                id=entity.id,
                stype_id=entity.stype_id,
                stype_name=entity.stype_name
            )
            for entity in entities
        ]
