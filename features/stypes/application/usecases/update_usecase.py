from features.stypes.application.contracts.update_contract import UpdateContract
from features.stypes.application.contracts.response_contract import StypeResponseContract
from features.stypes.infrastructure.stype_repository import StypeRepository
from features.stypes.domain.stype_entity import StypeEntity

class UpdateUseCase:

    def __init__(self, repo : StypeRepository):
        self.repo = repo

    def execute(self, contract : UpdateContract)->StypeResponseContract:
        entity = StypeEntity(
            id=contract.id,
            stype_id=contract.stype_id,
            stype_name=contract.stype_name
        )

        entity = self.repo.update(entity)

        return StypeResponseContract(
            id=entity.id,
            stype_id=entity.stype_id,
            stype_name=entity.stype_name
        )
        