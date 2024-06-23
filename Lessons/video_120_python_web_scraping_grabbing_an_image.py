# Now that we understand how to grab text information based on tags and element names, let's explore how to grab images from a site.
# Images on a website typically have their own URL link, ending in something like .jpg or .png
# Beautiful Soup can scan a page, locate the <img> tags and grab these urls.
# Then we can download the URLS as images and write them to the computer.
# Note: You should always check copyright permission before downloading and using an image from a website.

import requests
import bs4

res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")

soup = bs4.BeautifulSoup(res.text, "lxml")

computer_image = soup.select(".infobox-image img")[0] # Wiki changed a bit since the course was released so the class is not in the image anymore... I had to do some pseudo selection here to actually get the desired image.
print(f"Feature Image: {computer_image["src"]}")

image_link = requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg")
f = open("my_computer_image.jpg", 'wb')
f.write(image_link.content) #I forgot the .content
f.close()

