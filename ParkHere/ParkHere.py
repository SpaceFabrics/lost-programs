import requests
from bs4 import BeautifulSoup

req = requests.get('https://en.parkopedia.ca/parking/toronto/?arriving=202312152130&leaving=202312152330')
soup = BeautifulSoup(req.content, "html.parser")


print(soup.get_text())