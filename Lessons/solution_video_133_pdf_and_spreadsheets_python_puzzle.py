# Now, this is the course's solution:
import PyPDF2
import csv
import re
# my urls will look different
data = open("C:\\Users\\crstn\\OneDrive\\Desktop\\Myprojects\\Zero To Hero Course Files\\Course\\Complete-Python-3-Bootcamp\\15-PDFs-and-Spreadsheets\\Exercise_Files\\find_the_link.csv", encoding = "utf-8")

csv_data = csv.reader(data)

data_lines = list(csv_data)
# print(f"Data Lines: {data_lines}")
link_str = ""
for row_num, data in enumerate(data_lines) :
    link_str += data[row_num]

print(link_str) # = https://drive.google.com/open?id=1G6SEgg018UB4_4xsAJJ5TdzrhmXipr4Q

f = open("C:\\Users\\crstn\\OneDrive\\Desktop\\Myprojects\\Zero To Hero Course Files\\Course\\Complete-Python-3-Bootcamp\\15-PDFs-and-Spreadsheets\\Exercise_Files\\Find_the_Phone_Number.pdf", "rb")
pdf = PyPDF2.PdfReader(f)
pattern = r"\d{3}.\d{3}.\d{4}"
all_text = ""
for n in range(len(pdf.pages)) :
    page = pdf.pages[n]
    page_text = page.extract_text()

    all_text = all_text + " " + page_text

for match in re.finditer(pattern, all_text) :
     print(match)
    
print(all_text[41808:41808+20])

# Bleh... matched it like crap. My solution is a bit better in terms of output. Im unsure about everythin else, though.... I basically used a dictionary to hold possible combinations of regex... Then did a j-loop to get to everything. Mine is still cracked because it returns 4 times for some reason.


# Course solution end...

# Additional note:
# Just doing some research on this enumerate business
# Convert a tuple into an enumerate object:
x = ('apple', 'banana', 'cherry')
y = enumerate(x)
print(y)
# Returns an enumerate object: <enumerate object at 0x000002C792DD9E40>

# Definition and Usage:
# The enumerate() function takes a collection such as a tuple, and returns it as an enumerate object.
# The enumerate function adds a counter as the key of the enumerate object
# Syntax: enumerate(iterable, start)

# ok... but what is it for?

# On programiz.com:
# The enumerate() function adds a counter to an iterable and erturns it as an enumerate object - an iterator with index and the value.

languages = ["Python", "Java", "Javascript"]

# enumerate the list
enumerated_languages = enumerate(languages)

# Convert enumerate object to a list
enumerated_languages_list = list(enumerated_languages)

print(enumerated_languages_list)
# Returns : [(0, 'Python'), (1, 'Java'), (2, 'Javascript')]
# So seemingly, each entry gets a key
print(enumerated_languages_list[0][1]) # Returns: Python
print(enumerated_languages_list[1][1]) # Returns: Java
print(enumerated_languages_list[2][1]) # Returns: Javascript

# This seems very powerful

