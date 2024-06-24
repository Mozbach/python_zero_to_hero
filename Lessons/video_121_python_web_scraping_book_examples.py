# We have seen how to grab elements one at a time, but realistically we want to be able to grab multiple elements, most likely across multiple pages.
# This is where we can combine our python knowledge with the web scraping libraries to create powerful scripts. 
# We will use a web scraping website called https://books.toscrape.com/
# We will practive grabbing elements across multiple pages.

# Goal: Get the title of every book with a 2-Star rating. 
import requests
import bs4

base_url = "https://books.toscrape.com/catalogue/page-{}.html"
# we can now use something like base_url.format("10") -> to give: https://books.toscrape.com/catalogue/page-10.html
# but then we maybe assign the page number to a variable: 
page_num = 10
# we can now use something like base_url.format(page_num) -> to give: https://books.toscrape.com/catalogue/page-10.html

res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text, "lxml")
product_pod = soup.select(".product_pod")
print(f"product_pod length: {len(product_pod)}")