from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bs4 import BeautifulSoup
import requests

# Pollutant readings are getting scrap with the beautiful soup library


@api_view(['GET'])
def get_readings(request):
    if request.method == 'GET':
        source = requests.get('https://air-quality.com/place/india/gurugram/d2853e61?lang=en&standard=aqi_us').text
        soup = BeautifulSoup(source, 'html.parser')
        list_of_pollutants = []
        articles = soup.find_all('div', class_='pollutant-item')
        for article in articles:
            pollutant = {}
            name = article.find('div', class_='name').text
            unit = article.find('div', class_='unit').text
            value = article.find('div', class_='value').text
            pollutant["name"] = name
            pollutant["value"] = value
            list_of_pollutants.append(pollutant)
        pollutants = {}
        pollutants["Gurugram"] = list_of_pollutants
        # print(pollutants)
        return Response(pollutants)
    return Response({"message": "Request Not Allowed"}, status=status.HTTP_400_BAD_REQUEST)



