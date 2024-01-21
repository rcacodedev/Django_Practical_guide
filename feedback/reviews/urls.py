from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReviewView.as_view(), name="review"),
    path("thankyou/", views.Thankyou.as_view(), name="thankyou"),
    path("reviews/", views.ReviewList.as_view(), name="reviews"),
    path("reviews/<int:pk>/", views.SingleReview.as_view(), name="single_review"),
]