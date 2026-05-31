from features.shared.repositories.base_repository import BaseRepository
from features.roles.domain.role_entity import RoleEntity

class RoleRepository(BaseRepository):

    def all(self)->list[RoleEntity]:
        return super().all()
    
    def getById(self, id)->RoleEntity:
        return super().getById(id)
    
    def getAllByColumns(self, entity)->list[RoleEntity]:
        return super().getAllByColumns(entity)

    def create(self, entity)->RoleEntity:
        return super().create(entity)
    
    def update(self, entity)->RoleEntity:
        return super().update(entity)