from apps.integrations.api_football import api_football

WORLD_CUP_ID = 1  # ID FIFA World Cup sur API-Football


def get_world_cup():
    data = api_football.get("leagues", params={"id": WORLD_CUP_ID})
    league = data["response"][0]["league"]
    seasons = data["response"][0]["seasons"]
    current_season = seasons[-1]["year"]
    return {
        "id": league["id"],
        "name": league["name"],
        "season": current_season,
    }
