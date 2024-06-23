# We already know how to open an individual file with Python, but we still don't knpow how to do a few things:
    # What if we have to open every file in a directory?
    #  What if we want to actually move files around on your computer?
# Python's OS module and shell utilities module (shutil) allow us to easily navigate files and directories on the computer and then perform actions on them such as moving them or deleting them.
# f = open('practice.txt', 'w+')
# f.write('This is a test string!')
# f.close()

# Let's now discuss the OS module:
# The os module is really useful because it helps you get the current directory, or list all the files in a directory
# And these commands will work across all operating systems
import os
# Get current directory
# print(f"Current Working Directory, os.getcwd: {os.getcwd()}") # Stands for get current working directory

# # Lets now LIST all the items in a directory
# print(f"List all items in current directory, os.listdir: {os.listdir()}")
# # Can I actually put all of these into a list?
# dirList = os.listdir()
# print(f"dirList: {dirList}") # Yes, yes you can
# Im just commenting out the above stuff, otherwise it gets a bit nuts in the terminal

# Lets move some items around using shutil 
import shutil
# shutil.move("practice.txt", "C:\\Users\\crstn\\OneDrive\\Desktop\Myprojects\\ZeroToHeroPython\\Lessons\\holdsTextFiles")
# I would really like to attempt this using the getcwd method and some concatenation....
# f = open("practiceMove", "w+")
# f.write("This is a new test String")
# f.close()

# shutil.move("practiceMove", "C:\\Users\\crstn\\OneDrive\\Desktop\Myprojects\\ZeroToHeroPython\\Lessons\\holdsTextFiles")

# Let's check to see that within the file using os.listdir()
print("READING THE FILES: ")
print(os.listdir("C:\\Users\\crstn\\OneDrive\\Desktop\\Myprojects\\ZeroToHeroPython\\Lessons\\holdsTextFiles"))

# Lets delete a file using 
# Three Ways, generally....
    # os.unlink(path), which deletes a file at the path you provide
    # os.rmdir(path), whcih deletes a folder (folder must be empty) at the path you provide
    # shutil.rmtree(path), this is the most dangerous, as it will remove all the files and folders contained in the path.
    # All of these methods can not be reversed. Which means if you make a mistake, you won't be able to recover the file. Instead we will use the send2trash module. A safer alternative that sends deleted fikles to the trash bin instead of permanent removal.
# Install the send2trash module with: pip install send2trash

# shutil.move("C:\\Users\\crstn\\OneDrive\\Desktop\\Myprojects\\ZeroToHeroPython\\Lessons\\holdsTextFiles\practiceMove.txt", "C:\\Users\\crstn\\OneDrive\\Desktop\\Myprojects\\ZeroToHeroPython\\Lessons")

import send2trash
# send2trash.send2trash('practiceMove.txt')
# print(os.listdir())

# os.walk
filepath = "C:\\Users\\crstn\\OneDrive\\Desktop\\Myprojects\\Zero To Hero Course Files\\Course\\Complete-Python-3-Bootcamp\\12-Advanced Python Modules\\Example_Top_Level"
for folder, sub_folders, files in os.walk(filepath) :
    print(f"Currently Looking at: {folder}")
    
    print("The Subfolders are: ")
    for sub_folder in sub_folders :
        print(f"\t> Subfolder: {sub_folder}")

    
    print("The Files Are: ")
    for f in files :
        print(f"\t>File: {f}")
    print("\n")