from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post

# Create your views here.
# Class Based View Post List
class PostLV(ListView):
    model = Post
    context_object_name = 'post_list'


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})
