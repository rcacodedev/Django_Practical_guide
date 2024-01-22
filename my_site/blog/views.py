from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post
from .forms import CommentForm

# def index(request):
    # posts = Post.objects.all().order_by("-date")[:3]
    # return render(request, "blog/index.html", {"posts": posts})
class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data
    
# def posts(request):
    # list_posts = Post.objects.all().order_by("-date")
    # return render(request, "blog/posts.html", {"all_posts": list_posts})

class AllPostsView(ListView):
    template_name = "blog/posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"

# def post_detail(request, slug):
    # identified_post = get_object_or_404(Post, slug=slug)
    # return render(request, "blog/post_detail.html", {"post": identified_post,
                                                    #  "post_tags": identified_post.tag.all()})
    
class SinglePostView(DetailView):
    template_name = "blog/post_detail.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tag.all()
        context["comment_form"] = CommentForm()
        return context
    
