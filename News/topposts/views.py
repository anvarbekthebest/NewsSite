from main.models import TopPost
from rest_framework import generics
from .serializers import TopPostSerializer

class TopPostList(generics.ListCreateAPIView):
    queryset = TopPost.objects.all()
    serializer_class = TopPostSerializer


class TopPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TopPost.objects.all()
    serializer_class = TopPostSerializer
    