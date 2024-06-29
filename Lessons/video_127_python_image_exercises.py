# IN the folder, "Working With Images", same folder this notebook is located in -> There are two images we will be working with:
    # word_matrix.png
    # my_mask.png
# The word_matrix.png image that contains a spreadsheet of words with a hidden message in it.
# Your task is to use the my_mask.png image to reveal the hidden message inside the word_matrix.png.
# Keep in mind, you may need to make changes to the my_mask.png in order for this to work. That is all clue we give you.
# This exercies is more open ended, so do not expect any guides, instead lettingh you explore and figure it out on your own.

# Now, for some reason, the .show() has a problem with the default png images that are stored in this location. They just don't work... So I just converted them from png to jpg...

from PIL import Image

my_mask = Image.open(r"C:\\Users\\crstn\\OneDrive\\Desktop\\Myprojects\\Zero To Hero Course Files\\Course\\Complete-Python-3-Bootcamp\\14-Working-With-Images\\mask.jpg").resize((1015, 559))
# Looks like it works well if you resize the image on import. So, maybe import future ones with the size in the title? like... my_mask_1025_500 -> gives a clear indication.
# But reassigning this to another variable just do not work.

word_matrix = Image.open(r"C:\\Users\\crstn\\OneDrive\\Desktop\\Myprojects\\Zero To Hero Course Files\\Course\\Complete-Python-3-Bootcamp\\14-Working-With-Images\\word_matrix.jpg")

# Imports Check...
# my_mask.show()
my_mask.putalpha(100)
# word_matrix.show()
# Imports Working...

# Taking my_mask and making it opaque.
# I might have to resize my_mask
print(f"my_mask_size: {my_mask.size}")
print(f"word_matrix_size: {word_matrix.size}")

print(f"my_mask size: {my_mask.size}")
print(f"word_matrix size: {word_matrix.size}")

# my_mask.resize((1015, 500))

word_matrix.paste(im = my_mask, box = (0, 0), mask = my_mask)

word_matrix.show()

# Ok... just resze the mask to the size of the word_matrix and make the image transparent to reveal: "Great Work With Images. You are the best.."
