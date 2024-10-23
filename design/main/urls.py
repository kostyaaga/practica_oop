from django.urls import path
from .views import index, login, singin

urlpatterns = [
    path('', index, name='index'),
    path('login', login, name='login'),
    path('singin', singin, name='singin'),
]
