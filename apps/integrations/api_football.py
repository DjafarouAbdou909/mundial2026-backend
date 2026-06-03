import requests
from django.conf import settings


class APIFootballClient:
    """Client HTTP pour API-Football v3."""

    BASE_URL = settings.API_FOOTBALL_BASE_URL

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "x-apisports-key": settings.API_FOOTBALL_KEY,
            "Accept": "application/json",
        })

    def get(self, endpoint: str, params: dict = None) -> dict:
        """
        Effectue un GET sur l'endpoint donné.
        Lève une exception si la réponse n'est pas 200.
        """
        url = f"{self.BASE_URL}/{endpoint}"
        response = self.session.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()


api_football = APIFootballClient()
