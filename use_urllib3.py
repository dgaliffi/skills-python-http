import json
import os
import webbrowser

import urllib3


nasa_api_key = os.environ.get('NASA_API_KEY')
api_url = f'https://api.nasa.gov/planetary/apod?api_key={nasa_api_key}'

def use_urllib3(api_url):

    http = urllib3.PoolManager()
    response = http.request('GET', api_url)
    json_response = json.loads(response.data)
    photo_url = json_response['url']
    webbrowser.open_new_tab(photo_url)

    return


if __name__== "__main__":
    use_urllib3(api_url)