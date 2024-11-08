from django.urls import path
from .views import index, rooms

urlpatterns = [
    path('', index, name="home"),
    path('rooms/', rooms, name="rooms"),
]