from django.urls import path

from . import views

urlpatterns = [
    path("", views.register, name="register"),
    path("complete/", views.register_complete, name="register_complete"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
]
