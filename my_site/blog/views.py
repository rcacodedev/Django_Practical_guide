from django.shortcuts import render, get_object_or_404

from .models import Post

def index(request):
    posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {"posts": posts})

def posts(request):
    list_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/posts.html", {"all_posts": list_posts})

def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post_detail.html", {"post": identified_post,
                                                     "post_tags": identified_post.tag.all()})