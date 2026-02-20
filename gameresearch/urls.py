from django.urls import path
from .views import game_search

urlpatterns = [
    path("", game_search, name="game_search"),
]
