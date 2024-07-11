from django.urls import path
from . import views

urlpatterns = [
    path('', views.twigos_home, name="twigo_home"),
    path("delete/<int:twigo_id>/", views.delete_twigo_post, name="delete_twigo_post"),
]