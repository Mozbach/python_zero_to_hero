# Inheritance and Polymorphism.
# Inheritance is basically a way to create new classes based on already existing classes.
# Gives the ability to re-use code one have already worked on and reduces the complexity of a program.

# First, lets create the Base Class - This is the main class similar to what we have been doing up until now.
class Animal() :
    def __init__(self) :
        print("Animal is Created")

    def who_am_i(self) :
        print("I am an animal..")
    
    def eat(self) :
        print("I am eating.")

# Now, create a new animal class, inheriting all of the Animal's defined methods:
# Since we place the Animal class within the parameters of the Dog class, the Dog class is deriving the methods from the Animal class, making the Dog a derived class - deriving off of the Animal class.
class Dog(Animal) :
    def __init__(self) :
        Animal.__init__(self)
        print("Dog is Created!")

    # One can re-write existing Base class methods:
    def who_am_i(self) :
        print("I am DOG!")
    # This will naturally not adjust the base class methods itself, but only for this derived clas.

# Creating a Cat class - my own discression
class Cat(Animal) :
    def __init__(self) :
        Animal.__init__(self)
        print("Cat created - meow!")

    # you can also add methods to the derived class
    def meow(self) :
        print("Meow-Meow HISSSS!")

myDog = Dog()
myCat = Cat()

myDog.who_am_i()
myCat.who_am_i()
myCat.meow()

# Polymorphism! According to the course, we won't be tested on it because it won't really be used until much later in the python journey.
# Polymorphism refers to the way in which different object classes can share the same method name. Those methods can then be called from the same place, even though a variety of different objects are passed in.

class Pig() :
    def __init__(self, name) :
        self.name = name

    def animal_call(self) :
        return " Says Squeel!"

    def speak(self) :
        return self.name + self.animal_call()
    

class Duck() :
    def __init__(self, name) :
        self.name = name

    def animal_call(self) :
        return " Says Quack!"

    def speak(self) :
        return self.name + self.animal_call()
    
niko = Pig(name="Niko")
felix = Duck(name="Felix")

print(niko.speak())
print(felix.speak())

# One way to demonstrate Polymorphism, is using a for-loop:
for pet in [niko, felix] :
    print(type(pet))
    print(pet.speak())

# Another way to demonstrate Polymorphism is with a Function, which is the more common way:
def pet_speak(pet) :
    print(pet.speak())

pet_speak(niko)
pet_speak(felix)

# Abstract class: A class that never expects to be instansiated to create an instance of this class, it is only designed to serve as a base class
class Animal() :
    def __init__(self, name) :
        self.name = name

    def speak(self) :
        raise NotImplementedError("Subclass must implemenet this abstract method.")

# The reason this Animal class does nothing is because it is supposed to only serve as a base class - This is what we call an Abstract Class.
# In the base class itself, it does not actually do anything, it is expecting you to inherit the Animal class, and then overwrite the speak() method when you create a new animal

class NewDog(Animal) :
    def speak(self) :
        return f"{self.name} Says Woof!"

charlie = NewDog("Charlie")
print(charlie.speak())