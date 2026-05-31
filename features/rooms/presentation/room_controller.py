from rest_framework.views import APIView, Request, Response
from rest_framework import status

from features.rooms.infrastructure.room_mapper import RoomMapper
from features.rooms.models import Room
from features.rooms.infrastructure.room_repository import RoomRepository
from features.rooms.application.services.room_service import RoomService
from features.rooms.presentation.room_serializers import RoomResponseSerializer, CreateSerializer, GetByColumnSerializer, UpdateSerializer
from features.rooms.application.contracts.create_contract import RoomCreateContract
from features.rooms.application.contracts.update_contract import RoomUpdateContract
from features.rooms.application.contracts.delete_contract import RoomDeleteContract
from features.rooms.application.contracts.getByColumn_contract import RoomGetByColumnContract
from features.rooms.application.contracts.getById_contract import GetRoomByIdContract


class RoomController(APIView):

    def __init__(self):
        self.repo = RoomRepository(Room , RoomMapper)
        self.service = RoomService(self.repo)
    
    def get(self, request : Request)->Response:

        if request.query_params:
            serializer = GetByColumnSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            contract = RoomGetByColumnContract(**serializer.validated_data)
            rooms = self.service.getByColumn(contract)
        else:
            rooms = self.service.allRooms()

        res = RoomResponseSerializer(rooms, many=True)

        return Response({
            "rooms" : res.data,
        }, status=status.HTTP_200_OK)
    
    def post(self, request : Request)->Response:
        serializer = CreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        contract = RoomCreateContract(**serializer.validated_data)
        
        res = self.service.createRoom(contract)

        return Response({
            "room" : RoomResponseSerializer(res).data,
            "message" : "Created Successfully!"
        }, status=status.HTTP_200_OK)
    
    def put(self, request: Request, id:int)->Response:
        serializer = UpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        contract = RoomUpdateContract(id=id, **serializer.validated_data)
        print("this is contract data : ",contract)
        res = self.service.updateRoom(contract)

        return Response({
            "room" : RoomResponseSerializer(res).data,
            "message" : "Updated successfully!"
        })
    
    def delete(self, request:Request, id:int)->Response:
        contract = RoomDeleteContract(id=id)
        res = self.service.deleteRoom(contract)

        if res:
            return Response({
                "message" : "Deleted! Successfully!"
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "message" : "Failed to delete!"
            }, status=status.HTTP_400_BAD_REQUEST)
        
class GetRoomByIdView(APIView):

    def __init__(self):
        self.repo = RoomRepository(Room, RoomMapper)
        self.service = RoomService(self.repo)

    def get(self, request:Request, id:int)->Response:

        contract = GetRoomByIdContract(id=id)
        room = self.service.getById(contract)

        return Response({
            "room" : RoomResponseSerializer(room).data
        })




        
        
