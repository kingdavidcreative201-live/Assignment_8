'''
This module contains functions for drawing polygons starting from where the turtle is currently located.
'''

import random


def square(t,length):
    """Draw a square with the given turtle t and side length."""
    for count in range(4):
        t.forward(length)
        t.left(90)

def hexgon(t,length):
    """Draw a hexagon with the given turtle t and side length."""
    for count in range(6):
        t.forward(length)
        t.left(60)

def radialHexagon(t,n,length):
    """Draw n hexagons with the given turtle t and side length, arranged radially."""
    for count in range(n):
        hexgon(t,length)
        t.left(360/n)

# this function further generalizes the radial pattern function to allow any shape to be drawn in a radial pattern
def radialPattern(t,n,length,shape):
    """Draw n shapes with the given turtle t and side length, arranged radially."""
    for count in range(n):
        shape(t,length)
        t.left(360/n)

def drawPattern(t, x, y, count, length, shape):
    """Draws a radial pattern with a random fill color at the given position."""
    t.begin_fill()
    t.up()
    t.goto(x, y)
    t.setheading(0)
    t.down()
    t.fillcolor(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
    radialPattern(t, count, length, shape)
    t.end_fill()
def circle(t, radius):
    """Draw a circle with the given turtle t and radius."""
    t.circle(radius)

