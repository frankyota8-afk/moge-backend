from django.urls import path
from features.departments.presentation.department_controller import DepartmentController, DepartmentListView, GetDepartmentByIdView

urlpatterns = [
    path("all/", DepartmentController.as_view()),
    path("create/", DepartmentController.as_view()),
    path("update/<int:id>/", DepartmentController.as_view()),
    path("delete/<int:id>/", DepartmentController.as_view()),
    path("search/<int:id>/", GetDepartmentByIdView.as_view()),
]