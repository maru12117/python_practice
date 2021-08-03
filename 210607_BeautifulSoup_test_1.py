from bs4 import BeautifulSoup
import requests

url = "https://www.daum.net/"
response = requests.get(url)
print(response)
