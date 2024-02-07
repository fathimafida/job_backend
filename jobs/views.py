from jobs.models import PostJob
from jobs.serializers import PostJobSerializer
from rest_framework import generics


class PostJobListAPIView(generics.ListCreateAPIView):
    queryset = PostJob.objects.all()
    serializer_class = PostJobSerializer


class PostJobDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostJob.objects.all()
    serializer_class = PostJobSerializer
