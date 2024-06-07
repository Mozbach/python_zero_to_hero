class Dog() :
    def __init__(self, name, breed, color, pelt) :
        self.name = name
        self.breed = breed
        self.color = color
        self.pelt = pelt

my_first_dog = Dog(name="Mool", breed="Pug", color="Beige", pelt="Short")
dogName = my_first_dog.name
dogBreed = my_first_dog.breed
dogColor = my_first_dog.color
peltType = my_first_dog.pelt
print(f"My dog's name is {dogName}. I think it is a {dogBreed}. Normally they have a {dogColor} {peltType} pelt.")

class MyPet() :
    def __init__(self, species, breed, color, age, name) :
        self.species = species
        self.breed = breed
        self.color = color
        self.age = age
        self.name = name

my_first_cat =  MyPet(species="Cat", breed="Tabby", color="Brown, black and grey", age=14, name="Alexi")
my_second_cat = MyPet(species="Cat", breed="Bombay", color="Black", age=4, name="Djinn")


# Turns out objects are not iterable... SO how does one then traverse them?/// In the famous words of Varg Vikerns -> "Let's Find Out!"