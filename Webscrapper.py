import requests
from bs4 import BeautifulSoup

# Enter the web address that you want to fetch 
page = requests.get("http://ict.siit.tu.ac.th/~stanislav/ComputerGraphics/")
soup = BeautifulSoup(page.content, 'html.parser')