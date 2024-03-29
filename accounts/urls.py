from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    profile,
    SignupView,
    Login
)

urlpatterns = [
    path('register/', SignupView.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('base/', profile, name='profile'),
]