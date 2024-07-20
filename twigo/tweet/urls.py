from django.urls import path
from . import views

urlpatterns = [
    path('', views.twigo_home, name="twigo_home"),
    path("delete/<int:twigo_id>/", views.delete_twigo_post, name="delete_twigo_post"),
    path("update/<int:twigo_id>/", views.update_twigo_post, name="update_twigo_post"),
    path("create/", views.create_twigo, name="create_twigo_post"),
    path("register/", views.register, name="register_user"),
]