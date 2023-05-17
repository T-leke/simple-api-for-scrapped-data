import requests
from bs4 import BeautifulSoup

url = """http://books.toscrape.com"""

response = requests.get(url)

html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')

#title = soup.find().get_text.strip()

title = soup.find("title").text

categories = soup.find(class = "nav nav-list").get_text


print(title)