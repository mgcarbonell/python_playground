import argparse
from datetime import datetime
import sys
from fractions import gcd
from PIL import Image
import random
import turtle
import math
import numpy as np

# A class that draws a spirograph


class Spiro:
    # constructor
    def __init__(self, xc, yc, col, R, r, l):

        # create own turtle
        self.t = turtle.Turtle()
        # set cursor shape
        self.t.shape('turtle')
        # set step in degrees
        self.step = 5
        # set drawing complete flag
        self.drawingComplete = False

        # set parameters
        self.setparams(xc, yc, col, R, r, l)

        # initiatize drawing
        self.restart()

    # set parameters
    def setparams(self, xc, yc, col, R, r, l):
        # spirograph parameters
        self.xc = xc
        self.yc = yc
        self.R = int(R)
        self.r = int(r)
        self.l = l
        self.col = col
        # reduce r/R to smallest form by dividing with GCD
        gcdVal = gcd(self.r, self.R)
        self.nRot = self.r // gcdVal
        # get ratio of radii
        self.k = r / float(R)
        # set color
        self.t.color(*col)
        # current angle
        self.a = 0

    # restart drawing
    def restart(self):
        # set flag
        self.drawingComplete = False
        # show turtle
        self.t.showturtle()
        # go to first point
        self.t.up()
        R, k, l = self.R, self.k, self.l
        a = 0.0
        x = R * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k))
        y = R * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k))
        self.t.setpos(self.xc + x, self.yc + y)
        self.t.down()

    # draw the whole thing
    def draw(self):
        # draw rest of points
        R, k, l = self.R, self.k, self.l
        for i in range(0, 360*self.nRot + 1, self.step):
            a = math.radians(i)
            x = R * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k))
            y = R * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k))
            self.t.setpos(self.xc + x, self.yc + y)
        # done - hide turtle
        self.t.hideturtle()

    # update by one step
    def update(self):
        # skip if done
        if self.drawingComplete:
            return
        # increment angle
        self.a += self.step
        # draw step
        R, k, l = self.R, self.k, self.l
        # set angle
        a = math.radians(self.a)
        x = self.R * ((1 - k) * math.cos(a) + l *
                      k * math.cos((1 - k) * a / k))
        y = self.R * ((1 - k) * math.sin(a) - l *
                      k * math.sin((1 - k) * a / k))
        self.t.setpos(self.xc + x, self.yc + y)
        # check if drawing is complete and set flag
        if self.a >= 360 * self.nRot:
            self.drawingComplete = True
            # done - hide turtle
            self.t.hideturtle()

    # clear everything
    def clear(self):
        self.t.clear()
