import json
import os
import webbrowser

import httpx


nasa_api_key = os.environ.get('NASA_API_KEY')
api_url = f'https://api.nasa.gov/planetary/apod?api_key={nasa_api_key}'


def use_httpx(api_url):

    request = httpx.get(api_url)
    json_request = request.json()
    photo_url = json_request['url']
    webbrowser.open_new_tab(photo_url)

    return


if __name__== "__main__":
    use_httpx(api_url)
