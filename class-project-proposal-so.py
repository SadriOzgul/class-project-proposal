print("Starting Turtle Draw For The Web")


from turtle import *

from math import atan2,degrees

setup(650,650)

def cbezto(b,c,d):
    a=pos()
    t=0.0
    while t < 1.0:
        t3 = t**3
        t2 = t**2
        f1 = -t3+3*t2-3*t+1
        f2 = 3*t3-6*t2+3*t
        f3 = -3*t3+3*t2
        f4 = t3
        x = a[0]*f1 + b[0]*f2 + c[0]*f3 + d[0]*f4
        y = a[1]*f1 + b[1]*f2 + c[1]*f3 + d[1]*f4
        d1 = -3*t2+6*t-3
        d2 = 9*t2-12*t+3
        d3 = -9*t2+6*t
        d4 = 3*t2
        dx = a[0]*d1 + b[0]*d2 + c[0]*d3 + d[0]*d4
        dy = a[1]*d1 + b[1]*d2 + c[1]*d3 + d[1]*d4
        angr = atan2(dy, dx)
        seth(degrees(angr))
        goto(x, y)
        t += 0.05
    goto(d)

up()
lt(108.1)
fd(225.2)
down()