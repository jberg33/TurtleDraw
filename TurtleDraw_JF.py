# JustinTheTurtle

# By: Justin Freiberg

import turtle
turtle.setup(450, 450)
TEXTFILENAME = 'JustinTheTurtle.txt'



print('JustinTheTurtle')

JustinTheTurtle = turtle.Turtle()
JustinTheTurtle.speed(10)
JustinTheTurtle.penup()

JustinTheTurtleTextfile = open(TEXTFILENAME, 'r')
line = JustinTheTurtleTextfile.readline()
while line:
    print(line, end='')
    parts = line.split(' ')

    if(len(parts) == 3):
        color = parts[0]
        x = int(parts[1])
        y = int(parts[2])

        JustinTheTurtle.color(color)
        JustinTheTurtle.goto(x,y)
        
        JustinTheTurtle.pendown()

    if (len(parts) == 1):
        JustinTheTurtle.penup()

    line = JustinTheTurtleTextfile.readline()

turtle.done()
JustinTheTurtleTextfile.close()



