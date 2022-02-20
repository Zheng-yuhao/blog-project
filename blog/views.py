from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post, Category, Tag
import markdown
import re


# Create your views here.

def index(request):
    # post_list = Post.objects.all().order_by('-created_time')
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', context={
        'post_list': post_list,
    })


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # if obj of Post in database has the pk, it will return the object, else, 404

    # post.body = markdown.markdown(post.body,
    #                               extensions=[
    #                                   'markdown.extensions.extra',
    #                                   'markdown.extensions.codehilite',
    #                                   'markdown.extensions.toc',
    #                               ])
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    post.body = md.convert(post.body)
    # if post.body do not have any contents, post.toc is not necessary to be displayed.
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''

    return render(request, 'blog/detail.html', context={'post': post})


def archive(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def category(request, pk):
    cate_obj = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate_obj).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def tag(request, pk):
    tag_obj = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=t).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})