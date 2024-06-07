class MyDog() :
    # Class Object Attribute
    # Same for any instance of a class
    species = "mammal"

    def __init__(self, breed, name, spots) :
        # Attributes
        # We take in the argument
        # Assign it using self.attribute_name
        self.breed = breed
        self.name = name

        # Expect a boolean
        self.spots = spots

    # Operaations and Actions ---> Methods
    def bark(self, number) :
        print(f"WOOF! My name is {self.name} and the number is {number}. Let's see if I have spots... {self.spots}. By that, it might be easier to assume my breed of {self.breed}.")

my_dog = MyDog(breed="Brown Dog", name = "Daniel", spots=False)
my_dog.bark(18)

class MyPet() :
    def __init__(self, species, breed, age, name, call) :
        self.species = species
        self.breed = breed
        self.age = age
        self.name = name
        self.call = call
    
    def myPetGreets(self, number) :
        print(f"{self.call}! My name is {self.name}. I am a {self.species} and I am of {self.breed} persuasion. I am {self.age} years old. This random number was assigned to me: {number}.")

myCat = MyPet(species="Cat", breed="Bombay", age=4, name="Djinn", call="Meow")

myCat.myPetGreets(20)

class Circle() :
# Class object attribute
    pi = 3.14
    def __init__(self, radius = 1) :
        self.radius = radius
        self.area = radius * radius * self.pi

    # Method
    def get_circumfrence(self) :
        return self.radius * self.pi * 2
    
first_circle = Circle(
    radius = 30
) 

print(f"My First Circle. Radius: {first_circle.radius}. Area: {first_circle.area}. Circumfence: {first_circle.get_circumfrence()}")