# sheesh...
# 1st Extercise: Use the requests library and BeautifulSoup to connect to http://quotes.toscrape.com/ and get the HTML text from the home page.
import requests
import bs4

base_url = "http://quotes.toscrape.com/page/{}"
home_html = requests.get(base_url.format(1)) 
soup = bs4.BeautifulSoup(home_html.text, "lxml")
# print(soup) # 1st Exercise complete

# 2nd Exercise: Get the names of all the Authors on the first page
author_set = set()
author_name = soup.select(".author")
# print(author_name)

for i in range(len(author_name)) :
    author_set.add(author_name[i].get_text())

print(f"Author's Length: {len(author_set)}")
print("Authors: ")
print(author_set)

# Exercise 2 Completed

# Exercise 3 - Create a LIST of all the quotes on the first page
quotes_list = []
# probably look something like ".text"
author_quotes = soup.select(".text")
# print(f"Author Quotes: {author_quotes}")
for i in range(0, len(author_quotes)) :
    quotes_list.append(author_quotes[i].get_text())
print(f"Author Quotes List: {quotes_list}")

# Exercise 3 completed

# Exercise 4 : Inspect the site and use Beautiful Soup to extract the top ten tags from the requests text shown on the top right from the home page.... 

top_ten_tags = []

top_ten_quotes = soup.select(".tag-item a") # it works here - by not down there.
print(f"Length of top ten quotes: {len(top_ten_quotes)}")

for i in range(len(top_ten_quotes)) :
    top_ten_tags.append(top_ten_quotes[i].get_text())
print(f"Top Ten Quotes: {top_ten_quotes}")