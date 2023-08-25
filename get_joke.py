import json
import requests

joke_url = 'https://icanhazdadjoke.com'


def get_joke(url: str) -> str:
    response = requests.get(url, headers={
        'Accept': 'application/json',
        'User-Agent': 'Learning Python Requests'}
                            )
    json_response = json.loads(response.text)
    ret_joke = json_response['joke']

    return ret_joke


if __name__ == "__main__":
    print(f'source: {joke_url}')

    joke = get_joke(joke_url)
    print(joke)
