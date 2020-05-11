from django.shortcuts import render
from .models import WeatherQuery
from bs4 import BeautifulSoup
import requests

# Create your views here.
def home(request):
    return render(request, 'home.html')

def search(request):
    location = request.POST.get('location')
    query = WeatherQuery(location = location)
    query.save()

    try:
        """
        First searching for the desired location and getting the required page's link.
        """

        primary_search_url  = 'https://www.timeanddate.com/weather/?query='+location.replace(" ",'')
        response1 = requests.get(primary_search_url)

        primary_soup = BeautifulSoup(response1.text, features='html.parser')

        query_results = primary_soup.find('div',{'class':'tb-scroll'})
        link = query_results.find('a').get('href')
        location_name = query_results.find('a').text


        """
        Then getting to the page containing the weather information of the desired location
        and scraping the content out.
        """

        secondary_search_url = 'https://www.timeanddate.com/'+link
        response2 = requests.get(secondary_search_url)

        secondary_soup = BeautifulSoup(response2.text, features='html.parser')

        temp_section = secondary_soup.find('div',{'id':'qlook', 'class':'three columns'})
        current_temp = temp_section.find(class_='h2').text
        current_condition = temp_section.find('p').text
        forecast = temp_section.find('span',{'title':'High and low forecasted temperature today'}).text
        img = temp_section.find('img',{'id':'cur-weather'}).get('src')


        #Getting all the relevant facts like visibilty, pressure, humidity...
        fact_section = secondary_soup.find('div',{'id':'qfacts', 'class':'five columns'}).findAll('p')[3:]
        facts={
            'Visibility':fact_section[0].text,
            'Pressure':fact_section[1].text,
            'Humidity':fact_section[2].text,
            'DewPoint':fact_section[3].text,
        }

        # Temperature data for upcoming hours
        upcoming_hours_temp_list = secondary_soup.find('table',{'id':'wt-5hr','class':'fw sep tc'})
        time = [time.text for time in upcoming_hours_temp_list.find('tr',{'class':'h2'}).findAll('td')]
        images_upcoming_hours = [img.get('src') for img in upcoming_hours_temp_list.findAll('img')]
        temp_upcoming_hours = [temp.text for temp in upcoming_hours_temp_list.find('tr',{'class':'h2 soft'}).findAll('td')]
        upcoming_hour_data = {
            'time':time,
            'images':images_upcoming_hours,
            'temp':temp_upcoming_hours,
        }

        weather_dict={
            'location':location_name,
            'current_temp':current_temp,
            'current_condition':current_condition,
            'forecast':forecast,
            'condition_img':img,
            'fact_section':facts,
            'upcoming_hour_data':upcoming_hour_data,
        }    
        
        return render(request, 'weather_query.html', weather_dict)

    except Exception:
        return render(request, 'weather_query.html', {'error': True})