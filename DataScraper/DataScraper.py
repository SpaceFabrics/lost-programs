from bs4 import BeautifulSoup 

url = 'https://etherscan.io/tokens'
soup = BeautifulSoup(url, 'html.parser')

div_bs4 = soup.find('div', id = "d-flex gap-1")
print(div_bs4)