from features.stypes.infrastructure.stype_repository import StypeRepository
from features.stypes.application.contracts.create_contract import CreateContract
from features.stypes.application.contracts.response_contract import StypeResponseContract

from features.stypes.domain.stype_entity import StypeEntity
from features.stypes.domain.exceptions import StypeAlreadyExistedException

class CreateUseCase:
    
    def __init__(self ,repo : StypeRepository):
        self.repo = repo

    def execute(self, contract : CreateContract)->StypeResponseContract:

        create_entity = StypeEntity(
            stype_name=contract.stype_name
        )
        if self.repo.existByName(create_entity):
            raise StypeAlreadyExistedException("Stype name has already existed!")
        else:
            create_entity.stype_id = self.repo.generateId("stype_id","STYPE")

        print("this is entity: ",create_entity) 
        response_entity = self.repo.create(create_entity)

        return StypeResponseContract(
            id=response_entity.id,
            stype_id=response_entity.stype_id,
            stype_name=response_entity.stype_name
        )
