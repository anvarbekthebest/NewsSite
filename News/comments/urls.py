from django.urls import path
from .views import CommentList, CommentDetail

urlpatterns = [
    path('<int:pk>/', CommentDetail.as_view()),
    path('', CommentList.as_view()),
]