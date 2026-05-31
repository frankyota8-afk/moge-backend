from rest_framework.views import APIView, Request, Response
from rest_framework import status

from features.stypes.infrastructure.stype_mapper import StypeMapper
from features.stypes.models import Stype
from features.stypes.infrastructure.stype_repository import StypeRepository
from features.stypes.application.services.stype_service import StypeService
from features.stypes.presentation.stype_serializers import StypeResponseSerializer, CreateSerializer, GetByColumnSerializer, UpdateSerializer
from features.stypes.application.contracts.create_contract import CreateContract
from features.stypes.application.contracts.update_contract import UpdateContract
from features.stypes.application.contracts.delete_contract import DeleteContract
from features.stypes.application.contracts.getByColumn_contract import GetByColumnContract
from features.stypes.application.contracts.getById_contract import GetByIdContract

class StypeController(APIView):

    def __init__(self):
        self.repo = StypeRepository(Stype , StypeMapper)
        self.service = StypeService(self.repo)
    
    def get(self, request : Request)->Response:

        if request.query_params:
            serializer = GetByColumnSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            contract = GetByColumnContract(**serializer.validated_data)
            stypes = self.service.getByColumn(contract)
        else:
            stypes = self.service.allStypes()

        res = StypeResponseSerializer(stypes, many=True)

        return Response({
            "stypes" : res.data
        }, status=status.HTTP_200_OK)
    
    def post(self, request : Request)->Response:
        serializer = CreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        contract = CreateContract(**serializer.validated_data)
        
        res = self.service.createStype(contract)

        return Response({
            "stype" : StypeResponseSerializer(res).data,
            "message" : "Created Successfully!"
        }, status=status.HTTP_200_OK)
    
    def put(self, request: Request, id:int)->Response:
        serializer = UpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        contract = UpdateContract(id=id, **serializer.validated_data)

        res = self.service.updateStype(contract)

        return Response({
                "stype" : StypeResponseSerializer(res).data,
                "message" : "Updated successfully!"
        })
    
    def delete(self, request:Request, id:int)->Response:
        contract = DeleteContract(id=id)
        res = self.service.deleteStype(contract)

        if res:
            return Response({
                "message" : "Deleted! Successfully!"

            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "message" : "Failed to delete!"
            }, status=status.HTTP_400_BAD_REQUEST)
        
class GetStypeByIdView(APIView):

    def __init__(self):
        self.repo = StypeRepository(Stype , StypeMapper)
        self.service = StypeService(self.repo)    

    def get(self, request: Request, id:int)->Response:
        
        contract = GetByIdContract(id=id)

        stype = self.service.getById(contract)

        return Response({
            "stype" : StypeResponseSerializer(stype).data
        })





        
        
