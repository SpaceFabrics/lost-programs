import requests 
from bs4 import BeautifulSoup 

html_text = requests.get('https://en.parkopedia.ca/parking/locations/toronto_ontario_canada_9f4edpz83df7unz52e/?arriving=202312150000&leaving=202312150200').text
print(html_text)
