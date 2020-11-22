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
        t1 = soup.select('.gray .p1')
        time_1 = t1[0].getText()
        w1 = soup.select('.temperature .p1')
        weather1 = w1[0].getText()
        t2 = soup.select('.gray .p2')
        time_2 = t2[0].getText()
        w2 = soup.select('.temperature .p2')
        weather2 = w2[0].getText()
        t3 = soup.select('.gray .p3')
        time_3 = t3[0].getText()
        w3 = soup.select('.temperature .p3')
        weather3 = w3[0].getText()
        t4 = soup.select('.gray .p4')
        time_4 = t4[0].getText()
        w4 = soup.select('.temperature .p4')
        weather4 = w4[0].getText()
        t5 = soup.select('.gray .p5')
        time_5 = t5[0].getText()
        w5 = soup.select('.temperature .p5')
        weather5 = w5[0].getText()
        t6 = soup.select('.gray .p6')
        time_6 = t6[0].getText()
        w6 = soup.select('.temperature .p6')
        weather6 = w6[0].getText()
        t7 = soup.select('.gray .p7')
        time_7 = t7[0].getText()
        w7 = soup.select('.temperature .p7')
        weather7 = w7[0].getText()
        t8 = soup.select('.gray .p8')
        time_8 = t8[0].getText()
        w8 = soup.select('.temperature .p8')
        weather8 = w8[0].getText()
        print('%-8s %-6s, %-6s' % ('Ночью:', time_1, time_2))
        print('%-8s %-6s, %-6s' % (' ', str(weather1), str(weather2)))
        print()
        print('%-8s %-6s, %-6s' % ('Утром:', time_3, time_4))
        print('%-8s %-6s, %-6s' % (' ', str(weather3), str(weather4)))
        print()
        print('%-8s %-6s, %-6s' % ('Днем:', time_5, time_6))
        print('%-8s %-6s, %-6s' % (' ', str(weather5), str(weather6)))
        print()
        print('%-8s %-6s, %-6s' % ('Вечером:', time_7, time_7))
        print('%-8s %-6s, %-6s' % (' ', str(weather7), str(weather8)))
        w = soup.select('.rSide .description')
        weather = w[0].getText()
        print(weather.strip())
    else:
        w1 = soup.select('.temperature .p1')
        weather1 = w1[0].getText()
        w2 = soup.select('.temperature .p2')
        weather2 = w2[0].getText()
        w3 = soup.select('.temperature .p3')
        weather3 = w3[0].getText()
        w4 = soup.select('.temperature .p4')
        weather4 = w4[0].getText()
        print('Ночью :' + weather1)
        print('Утром :' + weather2)
        print('Днём :' + weather3)
        print('Вечером :' + weather4)
        w = soup.select('.rSide .description')
        weather = w[0].getText()
        print(weather.strip())


weather_forecast()
print()
weather_forecast('львов', '2020-11-25')