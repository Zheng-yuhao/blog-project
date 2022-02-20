from blog.models import Post
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .forms import CommentForm
from django.contrib import messages


# comment is a function that can receive the comment post
# and also return the existed comments in database.
@require_POST  # Only can be used on POST requirement
def comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    form = CommentForm(request.POST)

    if form.is_valid():
        comment_obj = form.save(commit=False)
        comment_obj.post = post
        comment_obj.save()
        messages.add_message(request, messages.SUCCESS, 'Comments OK!', extra_tags='success')

        return redirect(post)  # because the get_absolute_url function can help us back to the detail url.

    # if the comment is not valid
    context = {
        'post': post,
        "form": form,
    }
    messages.add_message(request, messages.ERROR, 'Invalid comments!', extra_tags='danger')
    return render(request, 'comments/preview.html', context=context)