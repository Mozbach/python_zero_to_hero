# Task one : Use Python to extract the Google Drive link from the .csv file.
# Task two : Download the PDF from the Google Drive link. We already downloaded it for you just in case you can't download from Google Drive, and find the phone number that is in the document. Note... there are different ways of formatting a number.

import PyPDF2
import csv
import re

filepath = "C:\\Users\\crstn\\OneDrive\\Desktop\\Myprojects\\Zero To Hero Course Files\\Course\\Complete-Python-3-Bootcamp\\15-PDFs-and-Spreadsheets\\Exercise_Files\\"

find_the_link = open(f"{filepath}find_the_link.csv", encoding = "utf-8")

csv_data = csv.reader(find_the_link)

# Reformat csv into a list of python objects
data_lines = list(csv_data)


link_list = []

for i in range(len(data_lines)) :
    link_list.append(data_lines[i][i])

link_string = ""
for i in link_list :
    link_string = link_string + i

# print(link_string)
# Got the link and downloaded the pdf


pdf_file = open(f"{filepath}Find_the_Phone_Number.pdf", "rb")
pdf_reader = PyPDF2.PdfReader(pdf_file)
# print(len(pdf_reader.pages))

# Lets set up some regex patterns: 
pattern_dict = {
    "pattern1" : r"\d{3}\s\d{3}\s\d{4}", # number with digit pattern: 000 000 0000
    "pattern2" : r"\d{3}-\d{3}\s\d{4}", # number with digit pattern: 000-000-0000
    "pattern3" : r"\d{10}", # Number with digit pattern: 0000000000
    "pattern4" : r"\d{3}\s\d{4}\s\d{3}", # number with digit pattern 000 0000 000
    "pattern5" : r"\d{3}-\d{4}-\d{3}", # Number with digit pattern 000-0000-000
    "pattern6" : r"\d{3}\W\d{3}\W\d{4}", # Number with digit pattern 000.0000.000
    "pattern7" : r"\d{3}\W\d{4}\W\d{3}"
}

extracted_text = []
result = set()
for i in range(len(pdf_reader.pages)) :
    page = pdf_reader.pages[i].extract_text()
    extracted_text.append(page)
    for j in pattern_dict :
        
        for match in re.findall(pattern_dict[j], str(extracted_text)) :
                result.add(match)
        # Ok... nailed it essentially. Bit wonky. It returns 4 results... kinda on a loop of sort. So I just pump the result into a set to make sure I only get it once... Really wonder why this is happening, though...
print(result)