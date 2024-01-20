from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from django.views import View


class Review(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, "reviews/review.html", {"form": form})
    
    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thankyou/")

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

def thankyou(request):
    return render(request, "reviews/thankyou.html") 