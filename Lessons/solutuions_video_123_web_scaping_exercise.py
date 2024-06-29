# Course's solutions on the web scraping solutions - I'm excited to see what was doner in 4 and 5. I want to improve mine, but time.

import requests
import bs4

res = requests.get('http://quotes.toscrape.com')

# Get the names of all the authors on the first page
soup = bs4.BeautifulSoup(res.text, 'lxml')

soup.select('.author')

authors = set()
for name in soup.select(".author") :
    authors.add(name.text)
print(authors)

quotes = []
for quote in soup.select('.text') :
    quotes.append(quote.text)
    print(quote.text)

# Inspect the site and use beautiful soup to extract the tags from the request text.

# Create a List of all the quotes on the first page
for item in soup.select('.tag-item') :
    print(item.text)

# More than one page, but get all unique authors...

# First, lets do it using the knowledge that there are 10 pages.
url = "http://quotes.toscrape.com/page/"
authors = set()
for page in range(1, 10) :
    page_url = url + str(page)
    res = requests.get(page_url)
    soup = bs4.BeautifulSoup(res.text, "lxml")
    for name in soup.select(".author") :
        authors.add(name.text)

print("ALL THE AUTHORS")

# I actually had the thought of creating a range variable of massive number, then just check for something as soon as something... But yea, lets see what uncle does
# Look for "No quotes found" in text

page_url = url + str(999999999)
res =  requests.get(page_url)
soup = bs4.BeautifulSoup(res.text, "lxml")
print("No quotes found!" in res.text)

page_still_valid = True
authors = set()
page = 1

while page_still_valid :
    page_url = url + str(page)

    res = requests.get(page_url)

    if "No quotes found!" in res.text :
        break

    soup = bs4.BeautifulSoup(res.text, "lxml") 

    for name in soup.select(".author") :
        authors.add(name.text)

    page = page + 1

print(authors)