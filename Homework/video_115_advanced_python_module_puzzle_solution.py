# Figured it out myself... but this is basically what the course did.
# Now granted, the lector's files and folders are within the same directory, i had a different place to where I moved the files to.
# First, Unzip the instructions:
import shutil
shutil.unpack_archive("location of the zipped file", "location to where to extract it")
# Open the Instructions.txt file:
with open('extracted_content/Instructions.txt') as f :
    content = f.read()
    print(content)

import re
pattern = r"\d{3}-\d{3}-\d{4}"

# Here we will create function that takes in the text file and searches that file for the pattern
def search(file, pattern = r"\d{3}-\d{3}-\d{4}") :
    f = open(file, 'r')
    text = f.read()

    if re.search(pattern, text) :
        return re.search(pattern, text)
    else :
        return ''
    
import os
results = []
for folder, sub_folders, files in os.walk(os.getcwd()+'\\extracted_content') :
    for f in files :
        full_path = folder + "\\" + f
        print(full_path)

        results.append(search(full_path))