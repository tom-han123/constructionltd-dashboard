from django.urls import path
from . import views

app_name = 'base'
urlpatterns = [
    path("register",views.register, name="registeration"),
    path("", views.loginpage, name="login"),
    path("forgotpwd", views.forgot, name="forgotpwd"),
    path("getotp", views.getotp, name="getotp"),
    path("resetpwd/<str:pk>", views.resetpwd, name="resetpwd"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("logout", views.logoutpage, name="logout"),
]