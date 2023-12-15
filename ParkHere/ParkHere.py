from lxml import html
import requests 
from bs4 import BeautifulSoup 

html_text = requests.get('https://en.parkopedia.ca/parking/locations/toronto_ontario_canada_9f4edpz83df7unz52e/?arriving=202312150000&leaving=202312150200').text
soup = BeautifulSoup(html_text, 'lxml')
tree = html.fromstring(html_text.content)

prices = tree.xpath()

print(spots)