import requests
from django.shortcuts import render

def game_search(request):
    query = request.GET.get("q", "")
    games = []

    if query:
        url = "https://www.cheapshark.com/api/1.0/games"
        params = {
            "title": query,
            "limit": 10,
        }
        res = requests.get(url, params=params, timeout=10)
        games = res.json()

    return render(request, "gameresearch/game_research.html", {
        "query": query,
        "games": games,
    })
