from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from jobs.models import PostJob
from jobs.serializers import PostJobListSerializer

# Create your views here.


class PostJobListView(APIView):
    def get(self, request):
        postList = PostJob.objects.all()
        postSerializer = PostJobListSerializer(postList, many=True)
        return Response(postSerializer.data)
    
class PostJobDetailView(APIView):
    def get(self, request,pk):
        postDetailViewList = PostJob.objects.get(id=pk)
        postDetailSerializer = PostJobListSerializer(postDetailViewList)
        return Response(postDetailSerializer.data)
