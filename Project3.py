#Turtle Graphics: Hypnotic Pattern
#Use a loop with the turtle graphics library to draw the design

import turtle
naw = turtle.Turtle()
pixle = 0
for i in range(50):
    naw.forward(pixle)
    naw.left(90)
    pixle += 10
turtle.exit()
