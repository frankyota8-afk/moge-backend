from django.urls import path

from features.roles.presentation.controller import RoleController, GetRoleByIdView

urlpatterns = [
    path("all/", RoleController.as_view(), name="allRoles"),
    path("create/", RoleController.as_view(), name="createRoles"),
    path("update/<int:id>/", RoleController.as_view(), name="updateRoles"),
    path("delete/<int:id>/", RoleController.as_view(), name="deleteRoles"),
    path("search/", RoleController.as_view(), name="searchRoles"),
    path("search/<int:id>/", GetRoleByIdView.as_view())
]