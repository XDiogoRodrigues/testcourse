from django.urls import path

from .views import create_user, login

urlpatterns = [
    path('udemy-create-login', create_user, name='register'),
    path('udemy-login', login, name='login')
]
