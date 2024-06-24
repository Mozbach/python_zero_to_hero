# Previously on Python Ball Z - Goal was to get the title of every book with a 2-Star rating.

import requests
import bs4

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

page_num = 10
# We can now use something like base_url.format("10") -? to give  "https://books.toscrape.com/catalogue/page-10.html"

res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text, "lxml")
products = soup.select(".product_pod")
example = products[0]
print(example)

# Generally, say we want to find the titles of books with 2 - star ratings, there are more than 2, but here is 2 ways of doing it:
print(f"{'star-rating Three' in str(example)}") # This then returns True, because yes, 'star-rating Three' is in str(example). It would return False if not - obviously

# BUT, this method is not always efficient...
# Select specific classes using example.select(...)
print(f"star-rating Three example: {example.select('.star-rating.Three')}")
# This then returns:
"""
star-rating Three example: [<p class="star-rating Three">
<i class="icon-star"></i>
<i class="icon-star"></i>
<i class="icon-star"></i>
<i class="icon-star"></i>
<i class="icon-star"></i>
</p>]
"""
# Now, lets grab the title of an element using example.select(...)
print(f"title: {example.select('a')[1]["title"]}") # Note, we use [1] to select the correct element, since there are 2 anchors available in the return of example. The title we are looking for is in the second. Then we can grab the attribute off of that anchor which we need... in this case - "title"
# This will return "title: A Light in the Attic"

# So, to run this through...
# We can check if something is 2 stars (string call in, example.select(ratring))
# and then use example.select("a")[1]["title"] to grab the book title

# Now lets use a for loop to loop through all the pages and grab the desired titles
two_star_titles = []
one_star_titles = []
three_star_titles = []
# for n in range(1, 51) : # range(1, 51) because I want pages 1 - 51
#     scrape_url = base_url.format(n)
#     res = requests.get(scrape_url)

#     soup = bs4.BeautifulSoup(res.text, "lxml")
#     books = soup.select(".product_pod")

#     for book in books :
#         if len(book.select(".star-rating.Two")) != 0 :
#             book_title = book.select('a')[1]['title']
#             two_star_titles.append(book_title)
# print(f"Two Star Titles: {two_star_titles}")
# Well, the above works... It just takes a small while to return

# for n in range(1, 51) :
#     scrape_url = base_url.format(n)
#     res = requests.get(scrape_url)

#     soup = bs4.BeautifulSoup(res.text, 'lxml')
#     books = soup.select(".product_pod")

#     for book in books :
#         if len(book.select(".star-rating.One")) != 0 :
#             book_title = book.select("a")[1]["title"]
#             one_star_titles.append(book_title)
# print(f"One Star Title: {one_star_titles}")

for n in range(1, 51) :
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text, "lxml")
    books = soup.select(".product_pod")

    for book in books :
        if len(book.select(".star-rating.Three")) != 0 :
            book_title = book.select("a")[1]["title"]
            three_star_titles.append(book_title)
print(f"Three Star Titles: {three_star_titles}")