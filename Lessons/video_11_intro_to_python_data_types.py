# Integers: int -> Basic whole numbers, such as 3, 300, 200
int1 = int(3)
int2 = int(300)
int3 = int(200)

# Floating Points: float -> Any number with a deciaml point, such as 3.2, 300.4, 1.56
float1 = float(2.5)
float2 = float("2.7") # This will auto convert from string to float
float3 = float(4) # This will auto convert from an int(4) to a float(4.0)

# Strings: str -> Ordered sequence of characters, such as "This is a string", "200", '௹'
str1 = str("Hello, world")
str2 = str("2000.90")
str3 = str("... you get it")

#Lists: list -> Ordered sequence of objects, such as [10, "String in object", "900", 90.33]
list1 = list[1, 2, 3, 4, 5]
list2 = list[str1, str2, str3]
list3 = list[10, str3, float2, int1]

# Dictrionaries: dict -> Unordered Key:Value pairs, such as {"name": "Carsten", "surname": "Niemand"} 
dict1 = dict
{
    "Name": "Carsten",
    "Surname": "Niemand",
    "Age": "35",
    "Nailing This": "Duh"
}

# Tuples: tup -> Ordered immutable sequence of objects, such as (10, "Immutable String", 200.3)
tup1 = (10, "Immutable tuple string", 200.4)

# Sets: set -> Unordered collection of unique objects {"a", "b"}
set1 = {"a", "b"}

# Booleans: bool -> Logical value indicating either True or False
if 10 < 99 :
    print("Yes, 10 is less than 99")
