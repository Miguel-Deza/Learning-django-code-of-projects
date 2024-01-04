from django.urls import path

# Create your views here.
from . import views 

urlpatterns = [
    path("exam", views.index),
]