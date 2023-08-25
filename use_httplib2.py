import json
import os
import webbrowser

import httplib2


nasa_api_key = os.environ.get('NASA_API_KEY')
api_url = f'https://api.nasa.gov/planetary/apod?api_key={nasa_api_key}'

def use_httplib2(api_url):

    http = httplib2.Http()

    # The response is sent as a 2-item tuple, with the content at index 1
    response = http.request(api_url)
    json_response = json.loads(response[1])
    photo_url = json_response['url']
    webbrowser.open_new_tab(photo_url)

    return


if __name__== "__main__":
    use_httplib2(api_url)