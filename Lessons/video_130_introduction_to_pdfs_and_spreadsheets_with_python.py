# Python has the ability to work with PDF files and spreadsheet files.
# In this section we will explore libraries that allow us to interact with these files.
# Note: We highly recommend you work in the same location as the lecture... probably won't. But that's fine... It helps my walk skills.

# CSV stands for comma separated variables and is a very popular output for spreadsheet programs.

# Example:
# Name, Hours, Rate
# David, 20, 15
# Claire, 40, 20

import os

filepath = "C:\\Users\\crstn\\OneDrive\\Desktop\\Myprojects\\Zero To Hero Course Files\\Course\\Complete-Python-3-Bootcamp\\15-PDFs-and-Spreadsheets\\"

# print(os.listdir(filepath)) Works

import csv

# First: open the file like any other
data = open(f"{filepath}example.csv", encoding = "utf-8" )

# Second: Call csv.reader on that csv file
csv_data = csv.reader(data)

#  Reformat it into a list of list python object
data_lines = list(csv_data)

# print(data_lines[0]) # Works!

# Loop through the list
# for line in data_lines[:5] :
#     print(line)

# Extract data from row 8:
print(data_lines[8])
# ['8', 'Kassey', 'Herion', 'kherion7@amazon.com', 'Female', '245.51.154.79', 'Zákynthos']

# Extract specific information out of this row
print(data_lines[8][4]) # This should then extract the gender
#  And he scores!

# Trying to print all items in row 8
for item in data_lines[8] :
    print(item)

# Get all emails in the document
all_mails = []

print("All Emails: ")
for line in data_lines[1:] :
    all_mails.append(line[3])
    # print(line[3]) # Works

# Create a list of the full names - name and surname

all_names = []
print("All Full Names")
for line in data_lines[1:] :
    all_names.append((line[1] + " " + line[2]))

for i in all_names :
    print(i)
#  Hah haa! It works... Pretty simple... (I'm celebrating because I nailed it pre demonstration)

# Now, let's reveal how to write to a csv file.

file_to_output = open('to_save_file.csv', mode="w", newline = "")
csv_writer = csv.writer(file_to_output, delimiter = ",")

csv_writer.writerow(['a', 'b', 'c', 'd'])
csv_writer.writerows([["1", "2", "3", "4"], ["5", "6", "7", "8"]])

# Close the file
file_to_output.close()

# Add rows to the existing file
f = open('to_save_file.csv', mode = "a", newline = "")
csv_writer = csv.writer(f)
csv_writer.writerows([["9", "10", "11", "12"], ["13", "14", "15", "16"]])
f.close() # Always remember to close the files.