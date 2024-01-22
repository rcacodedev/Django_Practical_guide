from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from .models import Review
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, FormView
from django.http import HttpResponseBadRequest

# class ReviewView(View):
    # def get(self, request):
        # form = ReviewForm()
        # return render(request, "reviews/review.html", {"form": form})
    # 
    # def post(self, request):
        # form = ReviewForm(request.POST)
        # if form.is_valid():
            # form.save()
            # return HttpResponseRedirect("/thankyou/")
# def reviews(request):
    # if request.method == "POST":
        # form = ReviewForm(request.POST)
        # if form.is_valid():
            # form.save()
            # review = Review(username=form.cleaned_data["username"], review_text=form.cleaned_data["review_text"], rating=form.cleaned_data["rating"]) No se usa con ModelForm
            # review.save()
            # return HttpResponseRedirect("/thankyou/")
    # else:
        # form = ReviewForm()
    # return render(request, "reviews/review.html", {"form": form})

# class ReviewView(FormView):
    # template_name = "reviews/review.html"
    # form_class = ReviewForm
    # success_url = "/thankyou/"
# 
    # def form_valid(self, form):
        # form.save()
        # return super().form_valid(form)

class ReviewView(CreateView):
    model = Review
    template_name = "reviews/review.html"
    form_class = ReviewForm
    success_url = "/thankyou/"

# def thankyou(request):
    # return render(request, "reviews/thankyou.html") 
class Thankyou(TemplateView):
    template_name = "reviews/thankyou.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Your review was submitted successfully!"
        return context

# class ReviewList(TemplateView):
    # template_name = "reviews/review_list.html"
# 
    # def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        # reviews = Review.objects.all()
        # context["reviews"] = reviews
        # return context

class ReviewList(ListView):
    model = Review
    template_name = "reviews/review_list.html"
    context_object_name = "reviews"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=4)
        return data

# class SingleReview(TemplateView):
    # template_name = "reviews/single_review.html"
# 
    # def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        # review = Review.objects.get(pk=kwargs["pk"])
        # context["review"] = review
        # return context
    
class SingleReview(DetailView):
    model = Review
    template_name = "reviews/single_review.html"
    context_object_name = "review"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get("favorite_review")
        context["is_favorite"] = favorite_id == str(loaded_review.id)
        return context

class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST.get("review_id")

        if review_id is not None:
            request.session["favorite_review"] = review_id
            return HttpResponseRedirect("/reviews/" + review_id)
        else:
            return HttpResponseBadRequest("No se proporcionó 'review_id' en la solicitud.")