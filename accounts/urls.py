from django.urls import path
from .views import signup, user_activate

urlpatterns = [
    path('signup', signup),
    path('<slug:username>/activate', user_activate )
]
