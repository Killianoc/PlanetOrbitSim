from turtle import *
from time import sleep
import math

G = -0.1
TF = 10

class System(object):

    def __init__(self):
        self.star = None
        self.planetList = []
        self.myTurtle = Turtle()
        self.myTurtle.ht()

    def addPlanet(self, p):
        self.planetList.append(p)

    def addSun(self, theStar):
        self.star = theStar

    def showPlanets(self):
        for i in self.planetList:
            print(i)

    def movePlanets(self):

        """ Move the planets """
        for p in self.planetList:
            p.movePos(p.getXPos() + TF * p.getXVel(), p.getYPos + TF * p.getYVel())

            rx = self.star.getXPos() - p.getXPos()
            ry = self.star.getYPos() - p.getYPos()
            r = math.sqrt(rx ** 2 + ry ** 2)

            aX = G * self.star.getMass() * rx / r ** 3
            aY = G * self.star.getMass() * ry / r ** 3

            p.setXVel(p.getXVel() + TF * aX)
            p.setYVel(p.getYVel() + TF * aY)

class Star(object):

    """ Initialise the star """
    def __init__(self):
        self.name = "Sun"
        self.r = 150.0
        self.m = 15000.0
        self.c = "yellow"
        self.x = 0
        self.y = 0

        """ Draw the sun """
        self.myTurtle = Turtle()
        self.myTurtle.up()
        self.myTurtle.goto(self.x, self.y)
        self.myTurtle.down()
        self.myTurtle.dot(self.r, self.c)
        

        # r = radius, m = mass, c = color

    def __str__(self):
        return self.name

    def getRad(self):
        return self.r

    def getMass(self):
        return self.m

    def getXPos(self):
        return self.x

    def getYPos(self):
        return self.y

class Planets(Star):

    """ Initialise the planets of the solar system """
    def __init__(self, name, rad, mass, color, dist, vX, vY):
        Star.__init__(self)
        self.name = name
        self.rad = rad
        self.mass = mass
        self.color = color
        self.dist = dist
        self.vX = vX
        self.vY = vY
        self.x = dist
        self.y = 0

        """ Initialise turtle and draw planets """
        self.myTurtle = Turtle()
        self.myTurtle.up()
        self.myTurtle.goto(self.x, self.y)
        self.myTurtle.down()
        self.myTurtle.dot(self.rad, self.color)

    """ Return planet name """
    def __str__(self):
        return self.name

    """ Get and return various elements of the planet """
    def getRad(self):
        return self.rad

    def getMass(self):
        return self.mass

    def getDist(self):
        return self.dist

    def getXPos(self):
        return self.x

    def getYPos(self):
        return self.y

    """ Move the planet """
    def movePos(self, newX, newY):
        self.x = newX
        self.y = newY
        self.myTurtle.goto(newx, newy)
        self.myTurtle.dot(self.rad, self.color)

    """ Get velocities """
    def getXVel(self):
        return self.vX

    def getYVel(self):
        return self.vY

    def setXVel(self, newvX, newvY):
        self.vX = newvX
        self.vY = newvY

def main():

    """ Initialise the solar system and sun """
    system = System()
    sun = Star()
    system.addSun(sun)

    """ Initialise the planets """
    p1 = Planets('P1', 19.5, 1000.0, "green", 0.25, 0.0, 2.0)
    system.addPlanet(p1)
    
    #p2 = Planets('P2', 47.5, 5000.0, "blue", 0.3, 0.0, 2.0)
    #system.addPlanet(p2)
    
    #p3 = Planets('P3', 50.0, 9000.0, "red", 0.5, 0.0, 1.63)
    #system.addPlanet(p3)
    
    #p4 = Planets('P4', 100.0, 49000.0, "purple", 0.7, 0.0, 1.0)
    #system.addPlanet(p4)

    cycles = 900
    for num in range(cycles):
        system.movePlanets()

main()
    
