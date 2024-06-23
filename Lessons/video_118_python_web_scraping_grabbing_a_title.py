# Grabbing a Page Title from any website
import requests
import bs4
result = requests.get("http://www.example.com")

print(type(result))
print(f"result.text: {result.text}")

soup = bs4.BeautifulSoup(result.text, "lxml")

page_title = soup.select("title")
print(f"Page Title: {page_title}")

page_paragraphs = soup.select("p")
print(f"Page Paragraphs: {page_paragraphs}")

page_h1s = soup.select("h1")
print(f"Page H1s: {page_h1s}")

# To then grab only the text, not the opening and closing tags as well...
print(f"Page Paragraphs Text Only: {page_paragraphs[0].get_text()}")

# To then grab only the text in the h1 tag, same thing....
print(f"H1 text only: {page_h1s[0].get_text()}")