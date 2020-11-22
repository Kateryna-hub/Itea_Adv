import requests
import bs4
from datetime import datetime
import geocoder
import json
g = geocoder.ip('me')
print(g[0])

today = datetime.now().strftime('%Y-%m-d')

send_url = 'https://ipinfo.io/json'
request = requests.get(send_url)
json_ = json.loads(request.text)
city = json_['city']
print(city)


url = 'https://sinoptik.ua/погода-' + 'харьков'
url1 = 'https://sinoptik.ua'
request_url = requests.get(url1)
soup = bs4.BeautifulSoup(request_url.text, "html.parser")
print(soup.prettify())
title = soup.title.text
print(title.split(',')[0])

