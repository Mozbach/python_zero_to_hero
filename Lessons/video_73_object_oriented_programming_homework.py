# Problem 1 - Must admit... these math problems really have it in for me...
# Fill in the Line Class Methods to accept coordinates as a pair of tuples and return the slope and distance of each line
class Line :
    def __init__(self, coor1 = (), coor2 = ()) :
        self.coor1 = coor1
        self.coor2 = coor2

        # Alternative unpacking: 
        # self.x1 = coor1[0]
        # self.x2 = coor2[0]
        # self.y1 = coor1[1]
        # self.y2 = coor2[1]

    def distance(self) :
        # x1 = self.coor1[0]
        # y1 = self.coor2[0]
        # x2 = self.coor1[1]
        # y2 = self.coor2[1]
        # xy1Total = x1 - y1
        # xy2Total = x2 - y2
        # xy1TotalSquared = xy1Total ** 2
        # xy2TotalSquared = xy2Total ** 2
        # sqrtThis = xy1TotalSquared + xy2TotalSquared
        # return sqrtThis ** 0.5
        # One line return ...
        return (((self.coor1[0] - self.coor2[0]) ** 2) + ((self.coor1[1] - self.coor2[1]) ** 2)) ** 0.5
        
    def slope(self) :
        # x1 = self.coor1[0]
        # y1 = self.coor1[1]
        # x2 = self.coor2[0]
        # y2 = self.coor2[1]
        # topLine = y2 - y1
        # botLine = x2 - x1
        # One line return ...
        return (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])
        
ytLine = Line(
    coor1 = (2, 2),
    coor2 = (-2, -3)
)
   
ytSlope = Line(
    coor1 = (2, -1),
    coor2 = (-2 , -3)
)
print("YT Tyt Distance: ", ytLine.distance()) # Correct!
print(f"Yt Tut Slope: {ytSlope.slope()}") # Correct!
# First question I have - is what is the actual question here....
# like... coor1 and coor2 what?

# Distance Formula....
# Gives us the distance between 2 given points on an x,y (plane/plain)?
# Distance formula looks like this:
# distance = square of : (x2 - x1)squared + (y2 - y1)squared
# (Why the order of x2, x1 and y2, y1 -> This is math, don't question, just follow.)
# if we have two points, in our case we will use tuples to be points... here is an example:
# (2, 2),   (-2, -3)
# label them individually within the tuples as such: 
# (x1, y1), (x2, y2)
# So, now we plug in the numbers to where they corrospond in the distance formula
# Let's just see if I am understanding this plug into the distance thing....
# sqrt(-2 - 2)squared + (-3, - 2)squared
# sqrt(-4)squared + (-5)squared
# (NOTE: To get the square of something, times the something by itself the total amount of times indicated by the square... so ... 2 in this case... 5 * 5 = 25... 4 * 4 = 16)
# NOTE: -something * -something will return a positive value... - * - = +
# sqrt(16) + (25)
# sqrt41
# Now, to try and get the square root of a number -> Not so simple as simply dividing it by itself...
# First: .. just know it.. There is not really a thing as taking the number you need the square root of to calculate the square root of it...
# You just kind of have to know that the square root of 25 is 5, because 5 x 5 = 25.... Makes coding this fucking tough -> Fuck it. Just import the math library and use the sqrt(number) method.
# One can also calculate the sqrt of a number using the ** operator. Like this: 41 ** 0.5: Note the 0.5... NB!... This will then give you the square root of a number. Just a small part of what is needed for the homework assignment...
# 41 ** 0.5 = 6.4031242374328485
# Cool... That worked. So now, to get the slope of a line...
# formula looks like this (y2 - y1) / (x2 - x1)
# I don't think these are direct y2, y1 and x2, x1 values... The 1's and 2's are smaller... kind of like a floor squared
# So first, we need to set up 2 points... P1 = (x1, y1) | P2 = (x2, y2)
# P1(x1, y1) | P2(x2, y2)
# P1(-2, -3) | P2(2,  -1)

def findSqrt(num) :
    return num ** 0.5

courseLine = Line((3, 2), (8, 10))
print(f"courseLine Line: {courseLine.distance()}") # Correct !
print(f"courseLine Slope: {courseLine.slope()}") # Correct !
# Example output:
# coordinate1 = (3, 2)
# coordinate2 = (8, 10)
# li = Line(coordinate1, coordinate2)
# li.distance() -> 9.433981132056603
# li.slope() -> 1.6

# Now for the cylinder one...
# Create a Cylinder class with methods to calculate the volume and surface areas


# First we gotta figure out how to get pi...

class Cylinder() :
    # pi = 3.141592653589793 -> Course uses the rounder version of pi, as below
    pi = 3.14
    def __init__(self, height = 1, radius = 1) :
        self.height = height
        self.radius = radius

    def volume(self) :
        return self.pi * (self.radius ** 2) * self.height

    def surface_area(self) :
        return ((2 * self.pi) * (self.radius ** 2) + (2 * self.pi) * (self.radius * self.height))

ytCylinder = Cylinder(height = 8, radius = 3)
print(f"ytCylinder Volume: {ytCylinder.volume()}")

courseCylinder = Cylinder(height = 2, radius = 3)
print(f"courseCylinder Volume: {courseCylinder.volume()}")
print(f"courseCylinder Surface Area: {courseCylinder.surface_area()}")
# This here below works
# pi = 3.141592653589793 use the rounder version of pi instead -> Not that I support it, it is just what the course is using
# pi = 3.14
# width = 3
# height = 8
# print(f"width squared2: {width ** 2} - should be 9")
# print(f"Width squared2 * height: {(width ** 2) * 8} - should be 72...")
# print(f"72 * pi: {((width ** 2) * 8) * pi}")
# print((pi * (width ** 2)) * height)

# Nailed ... Now it is time for the surface area of a Cylinder...
pi = 3.14
width = 3
height = 8

# Formula for Surface Area
# print(f"Surface Area of Width(3) and Height(8): {(2 * pi) * (width ** 2) + (2 * pi) * (width * height)}")
# WORKS! Now to just try the course's surface area!
# c = Cylinder(2, 3)
# c.volume() -> 56.52
# c.surface_area() -> 94.2