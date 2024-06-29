# In this lecture we will explore how to work with Images in Python
# We will use the Pillow library which is part of the PIL - Python Imaging Library, with easy function calls.
# We will need to install this additional library: 

# Filepath to the working folder - because this file is not CLOSE, I say
import os
working_dir = "C:\\Users\\crstn\\OneDrive\\Desktop\\Myprojects\\Zero To Hero Course Files\\Course\\Complete-Python-3-Bootcamp\\14-Working-With-Images"

from PIL import Image
mac = Image .open(r"C:\\Users\\crstn\\OneDrive\\Desktop\\Myprojects\\Zero To Hero Course Files\\Course\\Complete-Python-3-Bootcamp\\14-Working-With-Images\\example.jpg")
print(f"mac.size: mac.size {mac.size} || mac.name: {mac.filename}")

# mac.show()


# Crop Images
# mac.prop details. Returns a rectangular region from this image. This is a 4-tuple defining left, upper, right and lower pixel coordinate
# Top image's default value is 0 on x and y.
# You can then use x for moving horizontaly on the image
# And then use y to move vertically on the
# you then use h and w for height and width seetings on the rectangle.
# So, default is 0,0,0,0
cropped_mac = mac.crop((0, 0, 100, 100 ))
pencils_img = Image.open("C:\\Users\\crstn\\OneDrive\\Desktop\\Myprojects\\Zero To Hero Course Files\\Course\\Complete-Python-3-Bootcamp\\14-Working-With-Images\\pencils.jpg")

# Grab some pencils from the top corner
print(pencils_img.size)
# x and y indicates the starting point of the crop - the top left corner of it
x = 0
y = 0
# width and height will be then used to create crop rectangular shape according to the size you gave.
w = 1950 / 3
h = 1300 / 10


# pencils_img.crop((x, y, w ,h))

# Grab some pencils from the bottom:
x2 = 0
y2 = 1100

w2 = 1950 / 3
h2 = 1300
# pencils_img.crop((x2, y2, w2, h2)).show()

# # Function to do crop an image at a given x,y location
# Not completed - I just need to finish working on the course.
# def change_img_size(img_url, new_x, new_y, new_w, new_h) :
    
#     x = new_x
#     y = new_y
#     w = new_w / 3
#     h = new_h / 10
#     return img_url.crop((x, y, w, h ))

# new_img = change_img_size(pencils_img, 0, 0, 1950, 1300)
# new_img.show()
print(mac.size)
halfway = 1993 / 2
x3 = halfway - 200
w3 = halfway + 200

y = 800
h = 1257

# mac.crop((x3, y, w3, h)).show()

# Copy and pasting images
# computer = mac.crop((x3, y, w3, h))
# mac.paste(im=computer, box=(0, 0,))
# mac.paste(im=computer, box=(400, 0))
# mac.paste(im=computer, box=(400, 0))
# mac.paste(im=computer, box=(800, 0))
# mac.paste(im=computer, box=(1200, 0))
# mac.paste(im=computer, box=(1600, 0))

# mac.paste(im=computer, box=(0, 450,))
# mac.paste(im=computer, box=(400, 450))
# mac.paste(im=computer, box=(800, 450))
# mac.paste(im=computer, box=(1200, 450))
# mac.paste(im=computer, box=(1600, 450))

# mac.paste(im=computer, box=(0, 900,))
# mac.paste(im=computer, box=(400, 900))
# mac.paste(im=computer, box=(800, 900))
# mac.paste(im=computer, box=(1200, 900))
# mac.paste(im=computer, box=(1600, 900))
# mac.show()

# Color Transparenct
# RGBA System
red = Image.open("C:\\Users\\crstn\\OneDrive\\Desktop\\Myprojects\\Zero To Hero Course Files\\Course\\Complete-Python-3-Bootcamp\\14-Working-With-Images\\red_color.jpg")

blue = Image.open("C:\\Users\\crstn\\OneDrive\\Desktop\\Myprojects\\Zero To Hero Course Files\\Course\\Complete-Python-3-Bootcamp\\14-Working-With-Images\\blue_jpg_color.jpg")

red.putalpha(124)
# blue.putalpha(100)
# blue.show()
# red.show()

# Resize Images
red.resize((500, 120)).show() # Have to directly call the resize... I tried to resize and THEN call it... Didn't work.


# Ok, so on the opacity adjustments, make the adjustment first, THEN you call to show it.... Don't even assign the opaque version to a new variable.... seems like with .show() it isn't working all that well.

# opaque_blue = blue.putalpha(120)
# opaque_blue.show() This does not work...
blue.putalpha(100)
# blue.show() # -> This works

# Now, use the PASTE functionality to paste the red and the blue on top of each other. Essentially mixing the two semi transparent images to form a new mix of colours.

blue.paste(im=red, box=(50, 20), mask=red)

# blue.show()

# now, save the new image.
# blue.save("my_purple.png") # This will save it to the current directory, but a full path to a d dirrerent folder can naturally be called.

# Now, finally... time for the challenge...
