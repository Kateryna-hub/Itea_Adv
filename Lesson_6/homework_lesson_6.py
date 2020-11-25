import requests
import bs4
import json
from datetime import datetime
import datetime

# send_url = 'https://ipinfo.io/json'
# r = requests.get(send_url)
# j = json.loads(r.text)
# city = j['city']
# print(city)


def weather_forecast(city='', date_=str(datetime.date.today())):
    if city == '':
        url = 'https://sinoptik.ua'
    else:
        url = 'https://sinoptik.ua/погода-' + city + '/' + date_

    year, month, day = map(int, date_.split('-'))
    fixed_date = datetime.date(year, month, day)
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)

    request_url = requests.get(url)
    soup = bs4.BeautifulSoup(request_url.text, "html.parser")
    title = soup.title.text
    print(title.split(',')[0])

    if fixed_date <= tomorrow:
        for num_p in range(1, 9):
            teg1 = '.gray .p' + str(num_p)
            teg2 = '.temperature .p' + str(num_p)
            time = (soup.select(teg1))[0].getText()
            weather = (soup.select(teg2))[0].getText()
            print('%-8s  %-6s' % (time, weather))
        weather_ = (soup.select('.rSide .description'))[0].getText()
        print(weather_.strip())
    else:
        for num_p in range(1, 5):
            teg1 = '.gray .p' + str(num_p)
            teg2 = '.temperature .p' + str(num_p)
            time = (soup.select(teg1))[0].getText()
            weather = (soup.select(teg2))[0].getText()
            print('%-8s  %-6s' % (time, weather))
        weather_ = (soup.select('.rSide .description'))[0].getText()
        print(weather_.strip())


weather_forecast()
print()
weather_forecast('харьков', '2020-11-26')