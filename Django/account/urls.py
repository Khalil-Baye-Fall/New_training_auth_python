from django.urls import path
from .views import registerUser, homePage, loginUser

urlpatterns = [
    path('', homePage, name='home'),
    path('register/', registerUser, name='register'),
    path('login/', loginUser, name='login'),
]