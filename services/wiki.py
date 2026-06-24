from http.client import responses

import requests
def get_wiki(query):
    for lang in('ru', 'en'):
        url = f"https://{lang}.wikipedia.org/api/rest_v1/page/summary/{query}"

        response = requests.get(
        url,
        headers = {
            "User-Agent": "KostyaTelegramBot/1.0"
        }
        )

        print(response.status_code)

        if response.status_code != 200:
            return None

        data = response.json()

        return {
            "title": data.get("title"),
            "text": data.get("extract")
        }
