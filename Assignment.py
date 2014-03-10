from turtle import *
from time import sleep

""" Global variables for gravitational force and time factor """
G = 0.1
TF = 10
R = 0

""" Star function, there is only one star """
class Star(object):

    """ Initialise the star and set its values """
    def __init__(self):
        self.name = "myStar"
        self.r = 500.0
        self.m = 15000.0
        self.c = "yellow"
        # r = radius, m = mass, c = color

    """ Draw the star on the screen """
    def drawPlanet(self):
        t = Turtle()
        t.screen.screensize(2000, 2000)
        self.t = t
        self.t.ht()
        self.t.speed(100)
        self.t.penup()
        self.t.dot(self.r, self.c)
        print("The planet " + self.name + " has been drawn!")
        print(self.t.position())
    
""" Planets class """
class Planets(Star):
    pRadius = 0
    """ Initialise the planets and set each of their values """
    def __init__(self, name, r, m, c, dist, v):
        Star.__init__(self)
        self.name = name
        self.r = r
        self.m = m
        self.c = c
        self.dist = dist
        self.v = v
        Planets.drawPlanet(self)
        Planets.addPlanet(self, self.r)


        #name, r = radius, m = mass, c = color, dist = distance, v = velocity

    def drawPlanet(self):
        """ Initiate turtle """
        t = Turtle()
        s = Star()
        
        self.t = t
        self.t.ht()
        self.t.speed(100)
        self.t.penup()
        self.t.setpos(s.r + self.r + self.dist + Planets.pRadius, 0.0)
        self.t.dot(self.r, self.c)
        print("Planet " + self.name + " has been drawn!")
        print("Previous radius: ", Planets.pRadius)
        print(self.t.position())

    def addPlanet(self, radius):
        self.radius = radius
        Planets.pRadius += self.radius

    def planetOrbit(self):
        s = Star()
        planetPos = self.t.position()
        self.prevV1 = self.v[1]
        self.t.clear()
        #self.t.setpos(s.r + self.r + self.dist + self.pRadius + self.v[0], self.prevV1 + self.v[1])
        #self.t.dot(self.r, self.c)
        """ Testing this function, not complete """


def main():

    """ Initiate the planets and sun """
    sun = Star()
    sun.drawPlanet()

    p1 = Planets('P1', 19.5, 1000.0, "green", 0.25, Vec2D(0.0, 2.0))
    p2 = Planets('P2', 47.5, 5000.0, "blue", 0.3, Vec2D(0.0, 2.0))
    p3 = Planets('P3', 50.0, 9000.0, "red", 0.5, Vec2D(0.0, 1.63))
    p4 = Planets('P4', 100.0, 49000.0, "purple", 0.7, Vec2D(0.0, 1.0))
    print("Final radius distance: ", Planets.pRadius)

    for i in range(0, 300):
        for j in range(0, TF):
            onclick(Planets.planetOrbit(p1))

    return ("Done!")

msg = main()
print(msg)
