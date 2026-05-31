from django.urls import path
from features.ranks.presentation.rank_controller import RankController, GetRankByIdView

urlpatterns = [
    path("all/", RankController.as_view()),
    path("create/", RankController.as_view()),
    path("update/<int:id>/", RankController.as_view()),
    path("delete/<int:id>/", RankController.as_view()),
    path("search/", RankController.as_view()),
    path("search/<int:id>/", GetRankByIdView.as_view()),
]