from requests import get
from pprint import pprint as pp
import datetime

def get_titles():
    url= 'https://api.stackexchange.com/2.3/questions'
    params = {'tagged': 'Python',
              'sort': 'creation',
              'site': 'stackoverflow'}
    params['todate'] = datetime.date.today()
    params['fromdate'] = datetime.date.today() - datetime.timedelta(days=2)
    response = get(url, params=params).json()
    n = 1
    for el in response['items']:
        print(f"{n} - {el['title']}")
        n += 1


if __name__ == '__main__':
    get_titles()


