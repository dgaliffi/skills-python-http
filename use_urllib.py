import json
import os
import urllib.request
import webbrowser


nasa_api_key = os.environ.get('NASA_API_KEY')
api_url = f'https://api.nasa.gov/planetary/apod?api_key={nasa_api_key}'

def use_urllib(api_url):

    request = urllib.request.Request(api_url)
    with urllib.request.urlopen(request) as response:
        data = json.loads(response.read().decode("utf-8"))
        photo_url = data['url']
        webbrowser.open_new_tab(photo_url)

    return


if __name__== "__main__":
    use_urllib(api_url)