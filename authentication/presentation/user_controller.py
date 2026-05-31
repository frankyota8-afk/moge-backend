from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from authentication.application.user_service import UserService
from authentication.infrastructure.user_repository import UserRepository



class UserController(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = UserService(UserRepository())
    
    def get(self, request: Request, id:int = None):
        if id is None:
            users = self.service.all()
            return Response({
                "users" : [
                    u.__dict__ for u in users
                ]
            },status=status.HTTP_200_OK)
        
        user = self.service.getUserById(id=id)

        if not user:
            return Response(
                {"message" : "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        return Response(
            {"user" : user.__dict__},
            status=status.HTTP_200_OK
        )
    
    def delete(self, request: Request, id:int)->str:
        message = self.service.delete(id)

        return Response({
            "message" : message
        },status=status.HTTP_200_OK)