# We previously mentioned a big part of web scraping with the bs4 library is figuring out what string syntax to pass into the soup.select() method.
# Let's go through a table with some common examples - These make a lot of sense if you know CSS.
# <--------------------------------+-------------------------------------------------+>
# |  soup.select('div')            |   All Elements with a "div" tag                 |
# <--------------------------------+-------------------------------------------------+>
# |  soup.select('#some_id')       |   All Elements sontaining id="some_id"          |
# <--------------------------------+-------------------------------------------------+>
# |  soup.select('.some_class')    |   All Elements containing class="some_class"    |
# <--------------------------------+-------------------------------------------------+>
# |  soup.select('div span')       |   Any elements named span within a div element  |
# <--------------------------------+-------------------------------------------------+>
# |  soup.select('div > span')     |   Any elements named span directly within a div |
# <--------------------------------+-------------------------------------------------+>

import requests
import bs4
res = requests.get("https://en.wikipedia.org/wiki/John_Carmack")

soup = bs4.BeautifulSoup(res.text, "lxml")
vector_toc_text = soup.select(".vector-toc-text span")
print(f"vector-toc-text: {vector_toc_text}")

for i in vector_toc_text :
    print(i.text)