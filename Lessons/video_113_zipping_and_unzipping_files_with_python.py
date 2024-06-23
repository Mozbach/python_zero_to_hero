# f = open("fileone.txt", "w+")
# f.write("ONE FILE")
# f.close()

# f2 = open("filetwo.txt", "w+")
# f2.write("SECOND FILE")
# f2.close()

# f3 = open("filethree.txt", "w+")
# f3.write("THIRD FILE")
# f3.close()

# Above we are just creating 3 text files.

# Lets create an empty zipped file
import zipfile
comp_file = zipfile.ZipFile("comp_file.zip", "w")

comp_file.write('fileone.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('filetwo.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('filethree.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

# Ok... it worked this time.
# To unzip file contents, you basically create a new file with the extractall method.
# SO, create an object to represent the zipped file, open it with "r", then use the extractall method on it, within the extractall method's parameters, provide a path to the file you want to unzip the files to. In this case I simply referenced a file named "extracted_files" which led to the creation of the folder, because it was not in the directory. Simple -> For some reason, this did not work before I took a nap.
# zip_obj = zipfile.ZipFile('comp_file.zip', 'r')
# zip_obj.extractall('extracted_files_2')


# Ok, but apparently the shell utility tool is better to do things like this. Let's find out
import shutil
# Lets take the "extracted_files" folder I previously created and zip the entire thing.
dir_to_zip = "C:\\Users\\crstn\\OneDrive\\Desktop\\Myprojects\\ZeroToHeroPython\\Lessons\\extracted_files" 
output_filename = "example_zip"

shutil.make_archive(output_filename, "zip", dir_to_zip)

# Now, lets use shutil to extract files
shutil.unpack_archive("example_zip.zip", "final_unzip", "zip")