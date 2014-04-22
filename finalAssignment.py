import math
from turtle import *

class Planet(object):

    def __init__(self, name, rad, mass, dist, color, vX, vY):

        """ Initialise the variables """
        self.name = name
        self.rad = rad
        self.mass = mass
        self.dist = dist
        self.color = color
        self.x = dist
        self.y = 0
        self.vX = vX
        self.vY = vY

        """ Set the turtle """
        self.mw = Turtle()
        self.mw.color(self.color)
        self.mw.shape("circle")

        """ Set the initial position of the sun """
        self.mw.up()
        self.mw.goto(self.x, self.y)
        self.mw.down()

    """ Getters and setters """
    def getName(self):
        return self.name

    def getRad(self):
        return self.rad

    def getMass(self):
        return self.mass

    def getDist(self):
        return self.dist

    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    def movePos(self, nX, nY):
        self.x = nX
        self.y = nY
        self.mw.goto(nX, nY)

    def getVX(self):
        return self.vX

    def getVY(self):
        return self.vY

    def setXV(self, newVX):
        self.vX = newVX

    def setYV(self, newVY):
        self.vY = newVY

class Sun(object):

    """ Initialise the sun class """
    def __init__(self):
        self.name = "Sun"
        self.rad = 150.0
        self.m = 15000.0
        self.c = "yellow"
        self.x = 0
        self.y = 0

        """Set the given position of each planet """
        self.mw = Turtle()
        self.mw.up()
        self.mw.goto(self.x, self.y)
        self.mw.down()
        self.mw.dot(self.rad, self.c)

    def getMass(self):
        return self.m

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return self.name

""" Solar system class """
class milkyWay(Planet):

    """ Initialise the solar system, keep track of each planet """
    def __init__(self, sun):
        self.star = None
        self.planets = []
        self.mw = Turtle()
        self.mw.ht()

    """ Add planets to the list, initialise the sun """
    def addPlanet(self, planet):
        self.planets.append(planet)

    def addSun(self, planet):
        self.star = planet

    def rotatePlanets(self):

        G = .1
        dt = 1

        """ Loop through each planet """
        for p in self.planets:

            """ Move the planet """
            p.movePos(p.getX() + dt * p.getVX(),
                      p.getY() + dt * p.getVY())

            rx = self.star.getX() - p.getX()
            ry = self.star.getY() - p.getY()

            """ Pythagoras theorom, to get distance """
            r = math.sqrt(rx ** 2 + ry ** 2)

            """ Calculate the acceleration of each planet """
            accX = G * self.star.getMass() * rx / r ** 3
            accY = G * self.star.getMass() * ry / r ** 3

            """ Calculate and set a new velocity of X and Y """
            p.setXV(p.getVX() + dt * accX)
            p.setYV(p.getVY() + dt * accY)

def initiateGalaxy():

    """ Create instances of each planet and the sun """
    sun = Sun()
    mw = milkyWay(sun)
    mw.addSun(sun)

    p1 = Planet("Planet 1", 19, 10, 220, "green", 0.0, 2.0)
    mw.addPlanet(p1)

    p2 = Planet("Planet 2", 50, 60, 300, "blue", 0.0, 2.0)
    mw.addPlanet(p2)

    p3 = Planet("Planet 3", 47, 50, 340, "red", 0.0, 1.63)
    mw.addPlanet(p3)

    p4 = Planet("Planet 4", 75, 100, 460, "purple", 0.0, 1.0)
    mw.addPlanet(p4)

    """ Initialise how many cycles the simulation should run for """
    timeFrame = 9000
    for m in range(timeFrame):
        mw.rotatePlanets()

initiateGalaxy()
    

    
