# To begin with pdf files, first install PyPDF2 at your cmd:
    # pip install PyPDF2

import os
import PyPDF2
filepath = "C:\\Users\\crstn\\OneDrive\\Desktop\\Myprojects\\Zero To Hero Course Files\\Course\\Complete-Python-3-Bootcamp\\15-PDFs-and-Spreadsheets\\"

# Few things was deprecated in the version of PyPDF2 I used, so this here is the keywords that work.
pdf_file_1 = open(f"{filepath}Working_Business_Proposal.pdf", "rb") 
pdf_reader = PyPDF2.PdfReader(pdf_file_1)
print(len(pdf_reader.pages))

page_one = pdf_reader.pages[0]
page_one_text = page_one.extract_text()
print(page_one_text)

# Hah ha! Works!
# Again, some keywords above had to change.

pdf_file_1.close()

# Ok, so writing to a pdf file:
    # We can only add pages to a pdf file
    # You can't add to text on the middle of a PDF file

pdf_file_1 = open(f"{filepath}Working_Business_Proposal.pdf", "rb")
pdf_reader = PyPDF2.PdfReader(pdf_file_1)

first_page = pdf_reader.pages[0]
# print("NEW F1 TEST!")
# print(first_page.extract_text())
# programatically grab pages from the pdf
# print("TYPE OF first_page")
# print(type(first_page))
pdf_writer = PyPDF2.PdfWriter()

pdf_output = open("Some new PDF Doc.pdf", "wb")

pdf_writer.write(pdf_output)
pdf_file_1.close()


# Simple example to grab all the text in a pdf file
pdf_file_1 = open(f"{filepath}Working_Business_Proposal.pdf", "rb")
pdf_text = []
pdf_reader = PyPDF2.PdfReader(pdf_file_1)
for num in range(len(pdf_reader.pages)) :
    page = pdf_reader.pages[num]

    pdf_text.append(page.extract_text())
print("All pdf_text")
print(pdf_text)