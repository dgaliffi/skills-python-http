import datetime
import json
import os
import webbrowser

import requests
from datetime import timedelta


nasa_api_key = os.environ.get('NASA_API_KEY')
api_url = f'https://api.nasa.gov/planetary/apod?api_key={nasa_api_key}'

def use_requests(api_url):

    response = requests.get(api_url)
    json_response = json.loads(response.text)
    photo_url = json_response['url']
    webbrowser.open_new_tab(photo_url)

    return


if __name__== "__main__":
    print(f'api_url = {api_url}')
    use_requests(api_url)

    x = datetime.date.today()
    day = timedelta(days=1)
    yesterday = x - day

    api_url_yesterday = api_url + f'&date={yesterday}'

    print(f'api_url = {api_url_yesterday}')
    use_requests(api_url_yesterday)