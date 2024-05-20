myfile = open("myfile.txt")
print(myfile.read())
myfile.seek(0)

print(myfile.read(10))
myfile.seek(0)

print(myfile.readline())
myfile.seek(0)

linelist = myfile.readlines()

print(linelist[1])
myfile.close()

distantfile = open("C:\\Users\\crstn\\OneDrive\\Desktop\\Myprojects\\ZeroToHeroPython\\holdsTextFiles\\textFile.txt")
print(distantfile.read())

with open("myfile.txt") as my_new_file :
    myfile_contents = my_new_file.read()

print(myfile_contents)

with open("C:\\Users\\crstn\\OneDrive\\Desktop\\Myprojects\\ZeroToHeroPython\\holdsTextFiles\\textFile.txt", mode="w") as my_distant_file :
    my_distant_file_contents = my_distant_file.write("This is new contents to the file\nThis should be on the second file of the new content\nand this should be on the third line")

print(my_distant_file_contents)

# Read and write to files
with open("created_file.txt", mode="w") as f :
    f.write("This file was created\nThis file was sculpted\nThis file was carved")

with open("created_file.txt", mode="a") as appendThis :
    appendThis.write("\nAnd this is appended finally")

with open("created_file.txt", mode="r") as read_new :
    read_new_contents = read_new.read()

print(read_new_contents)

with open("myfile.txt", mode="w") as ovrThis :
    ovrThis.write("I need this to be overwritten\nNot just appended\John Carmack and shit")

with open("myfile.txt", mode="r") as readThis :
    read_this_content = readThis.read()

print(read_this_content)