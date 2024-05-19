# Strings are immutable. So changing specific chars as: theString[3] = "f" -> Won't work
theString = "Pam"
newString = theString[1:]
finalString = "S" + newString
print(finalString)

x = "Hello World"
print(x + ", it is a good day - we will get this!")

z = "z"
print(z * 10)

# Here, unlike in js, we don't have automatic type conversion. So, for example : "2" + 2 will give an error
# But if you reassign the type manually, it is fine.
two = "2"
print(int(two) + 2)

print(x.upper())
print(x.lower())

print(x.split())
# Split can also split at individual letters in a string... by doing so it actually REMOVES those entries
print(x.split("l"))
