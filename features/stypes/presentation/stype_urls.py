from django.urls import path
from features.stypes.presentation.stype_controller import StypeController,GetStypeByIdView

urlpatterns = [
    path("all/", StypeController.as_view()),
    path("create/", StypeController.as_view()),
    path("update/<int:id>/", StypeController.as_view()),
    path("delete/<int:id>/", StypeController.as_view()),
    path("search/<int:id>/", GetStypeByIdView.as_view()),
]