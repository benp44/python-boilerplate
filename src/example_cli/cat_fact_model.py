import requests

API_URL = "https://cat-fact.herokuapp.com/facts/random"


def get_fact():
    try:
        with requests.get(API_URL) as response:
            response.raise_for_status()
            data = response.json()
            return data["text"]
    except Exception:
        return ""
