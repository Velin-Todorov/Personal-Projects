from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator

# Create your views here.

def post_list(request):
    posts = Post.published.all()

    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page', 1)

    posts = paginator.page(page_number)

    return render(
        request,
        'blog/post/list.html',
        {'posts': posts}
    )

def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug=post,
        status = Post.Status.PUBLISHED,
        publish__year = year,
        publish__month = month,
        publish__day = day
    )

    return render(
        request,
        'blog/post/detail.html',
        {'post': post}
    )