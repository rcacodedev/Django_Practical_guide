from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="index"),
    path("posts/", views.AllPostsView.as_view(), name="posts"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="post_detail"),
]