from django.urls import path
from . import views


urlpatterns = [
    path("", views.starting_page, name="stating-page"),
    path("login", views.views.login, name="login-page")
]