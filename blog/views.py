from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post


# Create your views here.

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={
        'post_list': post_list,
    })


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # if obj of Post in database has the pk, it will return the object, else, 404
    return render(request, 'blog/detail.html', context={'post':post})