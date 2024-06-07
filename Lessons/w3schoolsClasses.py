# Python Classes and Objects
# Pythin is an objects oriented programming language.
# Almost everything in pythin is an object, which is properties and methods.
# A class is like an object constructor, or a "blueprint" for creating objects.

# Create a class:
# To Create a class, use the "class" keyword:
class MyClass :
    x = 5

# Create Object
# Now we can use the class named MyClass to create objects:
# Create an object named P1 and print the value of x:
p1 = MyClass()
print(p1.x)

# The __ini__ function
# The examples above are classes and objects in their simplest for,, and are not really useful in real life applications.
# To understand the meaning of classes, we have to undestand the built-in __init__() function
# All classes have a function called __init__(), whici is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
# Create a class named Person, use the __init__() function to assign values for name and age:
class Person() :
    def __init__(self, name = "John" , age = 20) :
        self.name = name
        self.age = age

    def personGreet(self) :
        print(f"My name is {self.name}. I am about {self.age} years old.")

first_person = Person(name="Adam", age="40")

first_person.personGreet()

# The __init__() function is called automatically every time the class is being used to create a new object.

# The __str__() Function:
#  The __str__() controls what should be returned when the class object is represented as a string.
# If the __str__() function is not set, the string representation of the object is returned:
# The strin representation of an object WITHOUT the __str__() function
class Person2() :
    def __init__(self, name, age) :
        self.name = name
        self.age = age
    
p1 = Person2(name="Eve", age=29)

print(p1.name, p1.age)

# The string representation of an object WITH the __str__() function:

class Person3() :
    def __init__(self, name, age) :
        self.name = name
        self.age = age

    def __str__(self) :
        return f"{self.name}({self.age})"
    
p3 = Person3(name="Seth", age="19")

print(p3)

# Object Methods
# Objects can also contain methods. Methods in objects are functions that belong to the object.
# Lest's Create a method in the Person class:

class Person4() :
    def __init__(self, name="John", age=19, gender="Male", alive=True) :
        self.name = name
        self.age = age
        self.gender = gender
        self.alive = alive

    def person_greet(self) :
        print(f"Name: {self.name}. Age: {self.age}. Gender: {self.gender}. Living: {self.alive}")

p4 = Person4(
    name = "Carsten",
    age = 35,
    gender = "Male",
    alive = True
)

p4.person_greet()

# The __self__ parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

# The self parameter
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class.

# Date object Properties
# You can delete properties on objects by using the del keyword:
del p4.alive
# print(p4.alive)  Output: Error: p4 has no attribute 'alive'

# Delete entire objects using the del:
del p4
# print(p4)
# Output: NameError: name 'p4' is not defined. Did you mean 'p1'?

# The Pass Statement:
# class definitions cannot be empty, buit if you for some reason have a class definition with no content, put in the pass statement to avoid errors:
class EmptyClass() :
    pass

# That wraps it for the class section on w3schools.... after this there is still inheritence and so forth. But the course isn't there yet so here is just me running through what I know so far....
# - at the moment, still wondering how to do iteration related moves on a class...

class WorkForce() :
    # Global attribute:
    has_work = True
    minimum_salary = 5000
    manager = 'Marko'

    def __init__(
            self,
            name = "Jane",
            gender = "Female",
            duties = ['software developer', 'client onboarding'],
            salary = 45000,
            travel_allowance = False) :
        self.name = name
        self.gender = gender
        self.duties = duties
        self.salary = salary
        self.travel_allowance = travel_allowance

    def employee_duties(self) :
        duties = ""
        for i in self.duties :
            duties += f" | {i}"
        return duties
    
    def travel_allowance_check(self) :
        if self.travel_allowance :
            return "Yes"
        else :
            return "No"
        
    def employee_bio(self) :
        print(f"Name: {self.name}\nGender: {self.gender}\nDuties: {self.employee_duties()}\nSalry: {self.salary}\nTravel Allowance: {self.travel_allowance_check()}")
        

worker1 = WorkForce(
    name="Mary",
    gender="Female",
    duties=['tea', 'coffee', 'biscuits'],
    salary = 4000,
    travel_allowance=True
)

worker2 = WorkForce(
    name="Carsten",
    gender="Male",
    duties=["Full Stack Developer :D", "Dad", "Fitness Fiend", "Guitarist"],
    salary=25000,
    travel_allowance=False
)

print("Worker1:")
worker1.employee_bio()

print("\nWorker2:")
worker2.employee_bio()

class Pokemon() :
    species = "Pocket Monster"
    def __init__(
            self,
            name = "Bulbasaur",
            type = ["Grass", "Poison"],
            weakness = ["Fire", "Ice"],
            can_evolve = True,
            evolutions = ["Ivisaur", "Venusaur"],
            attacks = ["Leach Seed", "Tackle", "Vine Whip", "Razor Leaf"]
    ) :
        self.name = name
        self.type = type
        self.weakness = weakness
        self.can_evolve = can_evolve
        self.evolutions = evolutions
        self.attacks = attacks

    def loop_type(self) :
        typeString = ""
        for i in self.type :
            typeString += i + " | "
        return typeString

    def loop_weakness(self) :
        weaknessString = ""
        for i in self.weakness :
            weaknessString += i + " | "
        return weaknessString
        
    def evolutionBool(self) :
        if self.can_evolve :
            return "Yes"
        return "No"
    
    def loop_evolutions(self) :
        evolutionString = ""
        for i in evolutionString :
            if self.can_evolve :
                evolutionString += i + " | "
            else :
                evolutionString = "This Pokemon can't evolve."
        return evolutionString

    def loop_attacks(self) :
        attackString = ""
        for i in self.attacks :
            attackString += i + " | "
        return attackString
    
    def poke_bio(self) :
        print(f"*************{self.species}*************")
        print(f"Name: {self.name}")
        print(f"Type(s): {self.loop_type()}")
        print(f"Weaknesses: {self.loop_weakness()}")
        print(f"Evolveable: {self.evolutionBool()}")
        print(f"Evolutions: {self.loop_evolutions()}")
        print(f"Attacks: {self.loop_attacks()}")
        print("*****************************************")

charmander = Pokemon(
    name="Charmander",
    type=["Fire", "Lizard"],
    weakness=["Water", "Ground", "Rock"],
    can_evolve=True,
    evolutions=["Charmelion", "Charizard"],
    attacks=["Ember", "Scratch", "Tackle", "Flame Thrower"]
)

charmander.poke_bio()