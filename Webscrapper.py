import requests
from bs4 import BeautifulSoup

# Enter the web address that you want to fetch 
page = requests.get("http://ict.siit.tu.ac.th/~stanislav/ComputerGraphics/")
soup = BeautifulSoup(page.content, 'html.parser')

# Part of this code can also be used for DhiNLP to gather data from various documents online.
