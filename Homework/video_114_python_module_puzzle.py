# So here, we won't really tell you what you need to do.
# It is time to test your new skills, this puzzle project will combine multiple skill sets, including unzipping files with Python using os module to automatically search through lots of files.

# My goal is to figure it all out on my own.
# There is a .zip file called 'unzip_me_for_instructions', unzip it, open the .txt file with Python, read the instructions and see if you can figure out what you need to do.

import os
import re
import shutil

currentDir = os.getcwd()
print(f"Current Directory: {currentDir}")

mod_ex_dir = "C:\\Users\\crstn\\OneDrive\\Desktop\\Myprojects\\Zero To Hero Course Files\\Course\Complete-Python-3-Bootcamp\\12-Advanced Python Modules\\08-Advanced-Python-Module-Exercise"
unzip_this_file = "C:\\Users\\crstn\\OneDrive\\Desktop\\Myprojects\\Zero To Hero Course Files\\Course\Complete-Python-3-Bootcamp\\12-Advanced Python Modules\\08-Advanced-Python-Module-Exercise\\unzip_me_for_instructions.zip"
shutil.unpack_archive(unzip_this_file, "unzipped_instructions", "zip")

unzipped_instructions_dir = "C:\\Users\\crstn\\OneDrive\\Desktop\\Myprojects\\ZeroToHeroPython\\Homework\\unzipped_instructions\\extracted_content\\Instructions.txt"
challenge_file_dir = "C:\\Users\\crstn\\OneDrive\\Desktop\\Myprojects\\ZeroToHeroPython\\Homework\\unzipped_instructions\\extracted_content"
instructions = open(unzipped_instructions_dir, "r").read()
print(f"Opened Instructions: \n{instructions}")
# Ok, so I can give the opened file's contents to a string, then search it using the regex...

"""
Instructions was:
Good work on unzipping the file!
You should now see 5 folders, each with a lot of random .txt files.
Within one of these text files is a telephone number formated ###-###-####
Use the Python os module and regular expressions to iterate through each file, open it, and search for a telephone number.
Good luck!
"""
# Here we go...
# What is my plan here... try to loop through each folder and it's contents. This is really a next level one because it was not demonstrated in the course.
# Open the i file, check it for the pattern, if the pattern was not found, close it and move onto the next.
# Check out:
    # os.listdir()
    # os.walk()
# I think walk might be the answer...
# The regexpression to look for the phone number: 
# phone_number_pattern = re.finditer(r"\d{3}-\d{3}-\d{4}", instructions) # See here, instructions in the loop will be the opened file.
# Make an object out of the result using finditer
# The below works to traverse the folders, I am just uncommenting it to avoid the chaos in the terminal

for folder, subfolders, files in os.walk(challenge_file_dir) :
    print(f"Folder Name: {folder}")
    print("Files in Folder: ")
    for file in files :
        target_file = f"{folder}\{file}"

        opened_file = open(target_file, "r").read()
        for match in re.finditer(r"\d{3}-\d{3}-\d{4}", opened_file) :
            print(f"Found It! : {match}")
        
    print("\n")

"""
Folder Name: C:\Users\crstn\OneDrive\Desktop\Myprojects\ZeroToHeroPython\Homework\unzipped_instructions\extracted_content\Four
Files in Folder:
Found It! : <re.Match object; span=(1062, 1074), match='719-266-2837'>
"""
