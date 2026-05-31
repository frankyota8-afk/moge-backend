from rest_framework.views import APIView, Request, Response
from rest_framework import status

from features.ranks.infrastructure.rank_mapper import RankMapper
from features.ranks.models import Rank
from features.ranks.infrastructure.rank_repository import RankRepository
from features.ranks.application.services.rank_service import RankService
from features.ranks.presentation.rank_serializers import RankResponseSerializer, CreateSerializer, GetByColumnSerializer, UpdateSerializer
from features.ranks.application.contracts.create_contract import CreateContract
from features.ranks.application.contracts.update_contract import UpdateContract
from features.ranks.application.contracts.delete_contract import DeleteContract
from features.ranks.application.contracts.getByColumn_contract import GetByColumnContract
from features.ranks.application.contracts.getById_contract import GetByIdContract

class RankController(APIView):

    def __init__(self):
        self.repo = RankRepository(Rank , RankMapper)
        self.service = RankService(self.repo)
    
    def get(self, request : Request)->Response:

        if request.query_params:
            serializer = GetByColumnSerializer(request.data)
            serializer.is_valid(raise_exception=True)
            contract = GetByColumnContract(**serializer.validated_data)
            ranks = self.service.getByColumn(contract)
        else:
            ranks = self.service.allranks()

        res = RankResponseSerializer(ranks, many=True)

        return Response({
            "ranks" : res.data
        }, status=status.HTTP_200_OK)
    
    def post(self, request : Request)->Response:
        serializer = CreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        contract = CreateContract(**serializer.validated_data)
        
        res = self.service.createRank(contract)

        return Response({
            "rank" : RankResponseSerializer(res).data,
            "message" : "Created Successfully!"
        }, status=status.HTTP_200_OK)
    
    def put(self, request: Request, id:int)->Response:
        serializer = UpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        contract = UpdateContract(id=id, **serializer.validated_data)

        res = self.service.updateRank(contract)

        return Response({
            "rank" : RankResponseSerializer(res).data,
            "message" : "Updated successfully!"
        })
    
    def delete(self, request:Request, id:int)->Response:
        contract = DeleteContract(id=id)
        res = self.service.deleteRank(contract)

        if res:
            return Response({
                "message" : "Deleted! Successfully!"
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "data" : {
                    "message" : "Failed to delete!"
                }
            }, status=status.HTTP_400_BAD_REQUEST)
        
class GetRankByIdView(APIView):

    def __init__(self):
        self.repo = RankRepository(Rank, RankMapper)
        self.service = RankService(self.repo)

    def get(self, request :Request, id:int)->Response:
        contract = GetByIdContract(id=id)

        rank = self.service.getById(contract)

        return Response({
            "rank" : RankResponseSerializer(rank).data
        })



        
        
