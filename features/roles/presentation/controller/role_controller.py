from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from features.roles.application.services.role_services import RoleServices
from features.roles.infrastructure.role_repository import RoleRepository
from features.roles.models import Role
from features.roles.infrastructure.role_mapper import RoleMapper
from features.roles.presentation.serializer.create_serializer import CreateSerializer
from features.roles.presentation.serializer.response_serializer import RoleResponseSerializer
from features.roles.presentation.serializer.update_serializer import UpdateSerializer
from features.roles.presentation.serializer.getByColumn_serializer import GetByColumnSerializer

from features.roles.application.contracts.create_contract import CreateContract
from features.roles.application.contracts.delete_contract import DeleteContract
from features.roles.application.contracts.update_contract import UpdateContract
from features.roles.application.contracts.getByColumn_contract import GetByColumnContract
from features.roles.application.contracts.getById_contract import GetByIdContract
class RoleController(APIView):

    def __init__(self):
        self.repo = RoleRepository(Role, RoleMapper)
        self.service = RoleServices(self.repo)

    def get(self, request: Request):
        
        # If query params exist → SEARCH
        if request.query_params:
            serializer = GetByColumnSerializer(data=request.query_params)
            serializer.is_valid(raise_exception=True)

            contract = GetByColumnContract(**serializer.validated_data)
            roles = self.service.getByColumn(contract)

        else:
            # No params → GET ALL
            roles = self.service.allRoles()

        res = RoleResponseSerializer(roles, many=True)

        return Response({
            "roles": res.data
        })
    

    def post(self, request:Request):
        
        create_serializer = CreateSerializer(data=request.data)
        create_serializer.is_valid(raise_exception=True)
        contract = CreateContract(**create_serializer.validated_data)
        
        res = self.service.createRole(contract)

        response_serializer = RoleResponseSerializer(res)

        return Response({
            "data" : {
                "roles" : response_serializer.data,
                "message" : "Created Successfully!"
            }
        })
    
    def put(self, request: Request, id:int):
        serializer = UpdateSerializer(data=request.data)
        serializer.id = id
        serializer.is_valid(raise_exception=True)

        contract = UpdateContract(**serializer.validated_data)
        res = self.service.updateRole(contract)

        return Response({
            "data" : {
                "role" : RoleResponseSerializer(res).data,
                "message" : "Updated successfully!"
            }
        })
    
    def delete(self, request : Request, id:int):
        
        delete_contract = DeleteContract(id=id)
        
        if self.service.deleteRole(delete_contract):
            return Response({
                "message" : "Deleted successfully!"
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "data" : {
                    "message" : "Failed to delete!"
                }
            }, status=status.HTTP_400_BAD_REQUEST)
        
    
class GetRoleByIdView(APIView):

    def __init__(self):
        self.repo = RoleRepository(Role, RoleMapper)
        self.service = RoleServices(self.repo)

    def get(self, request: Request, id: int)->Response:
        contract = GetByIdContract(id=id)

        res = self.service.getById(contract)

        return Response({
            "role" : RoleResponseSerializer(res).data
        })


