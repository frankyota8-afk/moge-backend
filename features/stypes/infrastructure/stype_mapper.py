from features.stypes.domain.stype_entity import StypeEntity
from features.stypes.models import Stype


class StypeMapper:

    def toEntity(Stype : Stype)->StypeEntity:
        return StypeEntity(
            id=Stype.id,
            stype_id=Stype.stype_id,
            stype_name=Stype.stype_name
        )
    
    def toModel(entity : StypeEntity)->dict:
        return {
            "stype_id" : entity.stype_id,
            "stype_name" : entity.stype_name,
        }