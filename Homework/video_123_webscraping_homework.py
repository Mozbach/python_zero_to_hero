# sheesh...
# 1st Extercise: Use the requests library and BeautifulSoup to connect to http://quotes.toscrape.com/ and get the HTML text from the home page.
import requests
import bs4

base_url = "http://quotes.toscrape.com/"
total_html = requests.get(base_url)
soup = bs4.BeautifulSoup(total_html.text, "lxml")
print(soup)