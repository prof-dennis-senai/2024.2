from django.urls import path
from . import views

urlpatterns = [
    path('', lambda x: x+1),
]
