from django.urls import path
from . import views

urlpatterns = [
    path('', views.twigos_home, name="twigo_home")
]