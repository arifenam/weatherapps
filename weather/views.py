from django.shortcuts import render, HttpResponse
import requests
from bs4 import BeautifulSoup as bs


def weather_data(city):
    city = city.replace(' ','+')
    url = f'https://www.google.com/search?q=weather+of+{city}'
    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    LANGUAGE = 'en-US,en;q=0.9,ru;q=0.8'
    session = requests.Session()
    session.headers['accept-language']=LANGUAGE
    session.headers['user-agent']=USER_AGENT
    response = session.get(url)
    soup = bs(response.text, 'html.parser')
    #Get The Results
    result = {}
    result['location'] = soup.find('span',attrs='BBwThe').text
    result['daytime'] = soup.find('div',attrs='wob_dts').text
    result['weather'] = soup.find('span',attrs={'id':'wob_dc'}).text
    result['temp'] = soup.find('span',attrs={'id':'wob_tm'}).text
    print(result)
    return result

# Create your views here.

def home_view(request):
    if request.method == 'GET' and 'city' in request.GET:
        city = request.GET.get('city')
        results = weather_data(city)
        context={'results':results}
    else:
        context = {}

    return render(request, 'home.html', context)
