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

top_ten_quotes = soup.select(".tags-box .tag-item a") # it works here - by not down there.
print(f"Top Ten Quotes: {top_ten_quotes}")

for i in soup.find_all("a", href=True) :
    if "/" not in i['href'][5:-1] and i['href'][5:-1] != "" :
        print(i['href'][5:-1])
        top_ten_tags.append(i['href'][5:-1])
print(f"Top Ten Tags: {top_ten_tags}")

# Well, I mean - I don't think this is the answer they want - but it worked. so

# What is the last one in this:
# Exercise 5: Notice how there is more than one page, and subsequent pages look like this: http://quotes.toscrape.com/page2/. Use what you know about for loops and string concatenation to loop through all the pages and get all the unique authors on the website. Keep in mind there are many ways to achieve this, also note that you will need to somehow figure out how to check that your loop is on the last page with quptes. For debugging purposes, I will let you know that there are only 10 pages, so the last page is http://quotes.toscrape.com/page/10/, but try to create a loop that is robust enough that it would not matter to know the amount of pages beforehand, perhaps use try/except for this - I will definitely use try/except because I need practice with it.

# Get all the unique authors - use a set. (Duplicates not allowed!)
# So, first just try to do it for one page, then look back at the for loop in the book part to scrape tutorial to see how to jump through pages. This will be plenty simple.


