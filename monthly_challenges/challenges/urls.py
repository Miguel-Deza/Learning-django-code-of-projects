from django.urls import path

from . import views

# We config the url that we allow it this app
urlpatterns = [
    path("", views.index,  name="index"),
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]
