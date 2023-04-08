from django.urls import path
from .views import TopPostList, TopPostDetail

urlpatterns = [
    path('<int:pk>/', TopPostDetail.as_view()),
    path('', TopPostList.as_view()),
]