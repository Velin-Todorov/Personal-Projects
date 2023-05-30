from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmailPostForm
from django.core.mail import send_mail
from dotenv import load_dotenv
import os

load_dotenv()
get_env = os.getenv 

# Create your views here.
def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url()
            )

            subject = f"{cd['name']} recommends you read" \
                      f"{post.title}"
            
            message = f'Read {post.title} at {post_url}\n\n' \
                      f"{cd['name']}\'s comments: {cd['comments']}"
            

            send_mail(
                subject,
                message,
                get_env('EMAIL_HOST_USER'),
                [cd['to']]
            )
            sent = True

    else:
        form = EmailPostForm()
    
    return render(
        request, 
        'blog/post/share.html',
        {
            'post': post,
            'form': form,
            'sent': sent
        }
    ) 


def post_list(request):
    all_posts = Post.published.all()

    paginator = Paginator(all_posts, 3)
    page_number = request.GET.get('page', 1)

    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

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