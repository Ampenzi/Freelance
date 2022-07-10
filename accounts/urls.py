from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    SignupView,
    Login,
    profile,
)

urlpatterns = [
    path('register/', SignupView.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
]