from features.roles.domain.role_entity import RoleEntity
from features.roles.models import Role

class RoleMapper:

    def toEntity(role : Role)->RoleEntity:
        return RoleEntity(
            id=role.id,
            role_id=role.role_id,
            role_name=role.role_name
        )

    def toModel(role: RoleEntity)->dict:
        return {
            "role_id" : role.role_id ,
            "role_name" : role.role_name
        }