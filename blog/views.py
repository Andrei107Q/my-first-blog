from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.utils import timezone


def hello(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/hello.html', {'posts': posts})


def post_detail(request, pk):
    item = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})