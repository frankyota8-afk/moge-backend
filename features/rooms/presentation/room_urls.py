from django.urls import path
from features.rooms.presentation.room_controller import RoomController, GetRoomByIdView

urlpatterns = [
    path("all/", RoomController.as_view()),
    path("create/", RoomController.as_view()),
    path("update/<int:id>/", RoomController.as_view()),
    path("delete/<int:id>/", RoomController.as_view()),
    path("search/", RoomController.as_view()),
    path("search/<int:id>/", GetRoomByIdView.as_view()),
]