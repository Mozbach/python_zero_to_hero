# Additional Regex Syntax
# The "or" operator
import re

theString = "Where is my cat? My cat is black."
theString2 = "Where is my dog? He is white. And he ate a mouse in my house."
searchRes1 = re.search(r"cat", theString)
searchRes2 = re.findall(r"mouse|dog", theString2)
searchRes2Iter = re.finditer(r"mouse|dog", theString2)

print(f"searchRes2: {searchRes2}")
for match in searchRes2Iter :
    print(f"match in searchRes2Iter: {match}")
# print(f"searchRes2Iter: {searchRes2Iter}")

# Then, we also get the wildcard operator:
# The wildcard acts as a replacement to any character that might be there in that location
wildString = "This is a wildString - Aliskerov takes this!"
foundAll = re.findall(r"is", wildString)
print(foundAll)
# Get the iterm or letter right before the "is"
foundWilds = re.findall(r".is", wildString) # The . will return the item infront of the thing that is searched, and the thing that is searched will also be returned.
print(f"foundWilds: {foundWilds}") 
# You can also add additional wildcards to get the items infront of the searched item equal to how many wildcards is provided.
manyWilds = re.findall(r"..is", wildString) # This returns the 2 items before the searched item and the searched item.
print(f"manyWilds: {manyWilds}")

# Lets now discuss starts with and ends with
stringWithNumber = "7. I have a can and he is 7 years old. 99"
theFoundNumber = re.findall(r"^\d", stringWithNumber) # This will find a string that starts with a number.
print(f"theFoundNumber in stringWithNumber: {theFoundNumber}")
# Similarly, you can check if a string END with a number then return that number:
theEndNumber = re.findall(r"\d$", stringWithNumber)
print(f"The number at the end of stringWithNumber: {theEndNumber}")

# We can also use exclusion, which I will assume returns things that excludes a given pattern?
phrase = "There are 3 numbers 34 inside 4 this sentence."
# Lets attempt to exclude all digits in the prase variable
phrasePattern = r"[^\d]+" # Exclude the digits by wrapping the carrot symbol infront of the \d (digit) expression.
# The "+" behind the expression will put all the words back together, without it, it will return a giant list of every individual item taking up space in the search pattern.
seme = "this needs to be seperated"
def splitEverything(splitThis) :
    newArr = []
    for i in splitThis :
        newArr.append(i)
    return newArr
print(f"newArr: {splitEverything(seme)}")
# This is an example of what will happen if the "+" is not included in the search expression

phrasePatternFiltered = re.findall(phrasePattern, phrase)
print(f"phrase without the digits: {phrasePatternFiltered}")

# The carrot, ^ symbol is also good at filtering out punnctuation...
remove_punctuation_string = "This is a string, it has punctuation. I will qonquer the job!! Why is my cat so cute? - He must be hungry."
remove_punctuation_pattern = re.findall(r"[^,?.!-]+", remove_punctuation_string)
print(f"remove punctuation from a string: {remove_punctuation_pattern}")
# ... I want to try and take that string in turn it back into a sentence using something like join
def joinBack(toJoin) :
    return " ".join(toJoin)

print(f"Joined Pattern: {joinBack(remove_punctuation_pattern)}") # -> This works like a bomb!

# you can use the [brackets] for exclusion, but you can also use them for INCLUSION
inclusion_string = "Only find the hyphen-words in this sentence. But you don't know how long-ish they are?"
pattern = r"[\w]+-[\w]+"
print(f"inclusion string with pattern: {re.findall(pattern, inclusion_string)}")

# The parentheses can also be used for multiple options
options_text1 = "Hello, would you like some catfish?"
options_text2 = "Hello, would you like to take a catnap?"
options_text3 = "Hello, have you seen this caterpillar?"
options_pattern = r"cat(fish|nap|claw)"

for match in re.finditer(options_pattern, options_text1) :
    print(f"options_text1 search for fish : {match}")
# Returns: options_text1 search for fish : <re.Match object; span=(27, 34), match='catfish'>

for match in re.finditer(options_pattern, options_text2) :
    print(f"options_text2 search for nap : {match}")
# Returns: options_text2 search for nap : <re.Match object; span=(32, 38), match='catnap'>

for match in re.finditer(options_pattern, options_text3) :
    print(f"options_text3 search for claw : {match}")
# Rerturns nothing, because we are searching for eiter fish, nap or claw.