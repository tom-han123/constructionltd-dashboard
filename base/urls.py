from django.urls import path
from . import views

app_name = 'base'
urlpatterns = [
    path("register",views.register, name="registeration"),
    path("login", views.loginpage, name="login"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("logout", views.logoutpage, name="logout"),
]