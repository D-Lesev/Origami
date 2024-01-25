from django.urls import path
from .views import LoginView, BlogView, SignUpView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("", BlogView.as_view(), name="blog"),
    path("signup/", SignUpView.as_view(), name="signup"),
]
