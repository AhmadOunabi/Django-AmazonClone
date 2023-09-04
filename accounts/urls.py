from django.urls import path
from .views import signup, user_activate,profile

urlpatterns = [
    path('profile', profile),
    path('signup', signup),
    path('<slug:username>/activate', user_activate ),
]
