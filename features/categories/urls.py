from features.categories.views import CategoryView, GetCategoryByIdView

from rest_framework.urls import path

urlpatterns = [
    path("create/", CategoryView.as_view()),
    path("update/<int:id>/", CategoryView.as_view()),
    path("delete/<int:id>/", CategoryView.as_view()),
    path("all/", CategoryView.as_view()),
    path("search/<int:id>/", GetCategoryByIdView.as_view()),
]