from PIL import Image
words = Image.open(r"C:\\Users\\crstn\\OneDrive\\Desktop\\Myprojects\\Zero To Hero Course Files\\Course\\Complete-Python-3-Bootcamp\\14-Working-With-Images\\word_matrix.jpg")
mask = Image.open(r"C:\\Users\\crstn\\OneDrive\\Desktop\\Myprojects\\Zero To Hero Course Files\\Course\\Complete-Python-3-Bootcamp\\14-Working-With-Images\\mask.jpg")

# Resize the mask
print(words.size)
mask = mask.resize((1015, 559))
print(mask.size)
mask.putalpha(200)
# mask.show()

words.paste(mask, (0, 0), mask)
words.show()
# Opaque the mask

# Note the self reassignment -> This was one thing I didn't try...
# mask = mask.resize((..., ...)) -> Also note, it takes a tuple. Wonder if some tuple matching tricks can be used here...
