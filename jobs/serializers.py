from rest_framework import serializers
from .models import PostJob


class PostJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostJob
        fields = "__all__"
