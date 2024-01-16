from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"), # /challenges/
    path('<int:month>', views.monthly_challenges_by_number),
    path('<str:month>', views.monthly_challenges_function, name="month_challenge"),
]
