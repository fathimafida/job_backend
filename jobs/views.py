from jobs.models import PostJob
from jobs.serializers import PostJobSerializer
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class PostJobListAPIView(generics.ListCreateAPIView):
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["title", "place", "companyName"]
    queryset = PostJob.objects.all()
    serializer_class = PostJobSerializer


class PostJobDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostJob.objects.all()
    serializer_class = PostJobSerializer
