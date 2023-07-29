from django.urls import path
from posts.views import PostListView, PostDetailView
from . import views

urlpatterns = [
    path('', PostListView.as_view()),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail')
]