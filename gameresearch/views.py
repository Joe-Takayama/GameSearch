import requests
from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        query = request.GET.get("q", "")
        games = []

        if query:
            url = "https://www.cheapshark.com/api/1.0/games"
            params = {
                "title": query,
            }
            res = requests.get(url, params=params, timeout=10)
            games = res.json()

        return render(request, "gameresearch/game_research.html", {
            "query": query,
            "games": games,
        })
