from django.urls import path

from jobs.views import PostJobDetailAPIView, PostJobListAPIView


urlpatterns = [
    path("posts/", PostJobListAPIView.as_view()),
    path("posts/<int:pk>/", PostJobDetailAPIView.as_view()),
]
