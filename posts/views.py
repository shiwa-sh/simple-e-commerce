from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from posts.models import Post
from django.shortcuts import render


# Create your views here.
# def index(request):
#     temp = "<p>hello posts</p>"
#     return HttpResponse(temp)

class PostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"
