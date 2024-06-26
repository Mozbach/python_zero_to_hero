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

# Things to try:
# if " No quotes found! " --> stop loop or something

# Also maybe try to check if the .col-md-8 has div.quote, if not - stop loop or something

# Ended up going with if there is a class on the page called "next", increment the number, else break.

# Here is a basic regex to find the last item in the current url... so we will start it at 1, then increment it....
import re
# search_pattern = r"\d+"
# current_page = re.findall(search_pattern, current_url[:-1])
# current_page_num = str(current_page[0]) # is int initially because we need to compare it with i... maybe we can keep it a string but then do something like if i < int(current_page_num) : i += 1... 
# but no... What I want to do is to always keep i one less than the current page num
# print(current_page_num)
# new_res = requests.get(current_url)
# new_soup = bs4.BeautifulSoup(new_res.text, "lxml")
# select_author_from_soup = new_soup.select(".author")
# check_next = new_soup.select(".next")
# def next_checker(check_this) :
#     if check_this :
#         return True
#     else :
#         return False
# print(f"select_author_from_soup: {select_author_from_soup}")

def find_all_authors() :
    current_url ="https://quotes.toscrape.com/page/{}/" 
    all_author_set = set() 
    i = 0
    while i <= i + 1 :
        i += 1
        res = requests.get(current_url.format(i))
        soup = bs4.BeautifulSoup(res.text, "lxml") 
        if soup.select(".next") :
            q_num = 0
            for author in soup.select(".author") :
                    the_author = soup.select(".author")[q_num].get_text()
                    all_author_set.add(the_author)
                    q_num += 1
        else :
            # have to loop it once more for the last page... THEN break, otherwise we miss the entire last page.
            # There must be a better way than this
            q_num = 0
            for author in soup.select(".author") :
                    the_author = soup.select(".author")[q_num].get_text()
                    all_author_set.add(the_author)
                    q_num += 1
            break
        
    all_author_list = list(all_author_set)
    return(sorted(all_author_list))

print("Challenge 5 - Find all unique Authors on the Page! - DONE \m/")
for i in find_all_authors() :
     print(i)

# Hell Yea! I nailed this one! Took me long enough - but I nailed it! - No thanks, whatsoever to online resources
# See what I did by looping the for author in soup.select(".author") : -> then I create the_author?... That will also work to complete challenge 4 "properly..."

