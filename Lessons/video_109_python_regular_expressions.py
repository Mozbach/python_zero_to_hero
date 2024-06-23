# Well... I have tried regex before and I feel it is something you REALLY need to study - hard to actually get. Or at least something you should practice all the god damn time.
# But... here we go again.

# We already know that we can search for substrings within a larger string with the in operator:
    # "dog" in "my dog is great"
    #   > True
# This clearly has severe limitations, we need to know the exact string, and need to perform additional operations to account for capitalization and punctuation.
# What if we only know the pattern structure of the string we are looking for... like an email address or a phone number?

# Regular Expressions, or regex, allow us to search for general patterns in text data.
# For example, a simple email format can be:
    #  user@email.com
# We know in this case we are looking for a pattern like "text" + "@" + "text" + ".com"

# The re library allows us to create specialized pattern strings and then search for matches within text.
# The primary skill set for regex is understanding the special syntax for these pattern strings

# Don't necessarily need to memorize these patterns. Focus on understanding how to look up the information
# Phone number: > (000)-000-0000
# Regex Pattern: r"(\d\d\d)-\d\d\d-\d\d\d\d"
# But it will usually look more like this: r"(\d{3})-\d{3}-\d{4}

# This series of lectures will first focus on how to use the re library to search for patterns within text.
# Afterwards we will focus on understanding the regex syntax codes.

text = "The Agent's phone number is 408-555-1234. Call soon!"
print('phone' in text) # Returns True > Because yes, "phone" is in the text variable!

import re
pattern = 'phone'
print(re.search(pattern, text))
# Returns: <re.Match object; span=(12, 17), match='phone'>

pattern_not_in_text = "Carsten"
print(re.search(pattern_not_in_text, text))
# Returns: None

match = re.search(pattern, text)
# What is returned is called a "Regular Expression Match Object" -> And quite a bit of data can be gathered from it
print(match.span())
# Returns the actual index location of the span: (12, 17)

# You can also call match.start() : 12
# Also the match.end() : 17
# But we, unfortunately only get back the first match.

# BUT, we can use the findall(), which will then return all instances of the match.
text2 = "my phone first, my phone second!"
matches = re.findall(pattern ,text2)
print(f"all locations of {pattern} within {text2}: {matches}")
# This does not actually return the information, just a list of the matches...: []'phone', 'phone']

# So, we can get them back as objects:
for match in re.finditer(pattern, text2) : # This will iterate through text2 and then returns each match object that is found. 
    print(match)
# So, this is a bit better, as it returns more information about the returned match objects:
# <re.Match object; span=(3, 8), match='phone'>
# <re.Match object; span=(19, 24), match='phone'>