from django.urls import path
from . import views
urlpatterns = [
    path("register" , views.RegisterView.as_view() , name = "register"),
    path("login" , views.LoginView.as_view() , name = "login"),
    path("logout" , views.LogoutView.as_view() , name = "logout"),
    path("forget" , views.ForgetView.as_view() , name = "forget"),
    path("active-code/<code>" , views.Active_AcountView.as_view(), name = "active_code"),
    path("change-password/<code>" , views.ChangeView.as_view(), name = "change_password")
]