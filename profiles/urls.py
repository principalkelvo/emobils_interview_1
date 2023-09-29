from django.urls import path, re_path
from .views import (
    ProfileOwnerView
)

urlpatterns = [
    path('profile/me/', ProfileOwnerView.as_view(), name='profile-me'),
]