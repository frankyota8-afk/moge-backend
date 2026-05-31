from rest_framework.urls import path
from features.staffs.presentation.staff_controller import GetStaffByColumnView, StaffController, GetStaffByIdView

urlpatterns = [
    path("create/", StaffController.as_view()),
    path("update/<int:id>/", StaffController.as_view()),
    path("delete/<int:id>/", StaffController.as_view()),
    path("all/", StaffController.as_view()),
    path("search/<int:id>/", GetStaffByIdView.as_view()),
    path("search/", GetStaffByColumnView.as_view()),
]