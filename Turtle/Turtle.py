import turtle

#trapezoid

"""turtle.forward(100)
turtle.right(50)
turtle.color('blue')
turtle.forward(100)
turtle.left(50)
turtle.color('black')
turtle.backward(220)
turtle.right(125)
turtle.backward(90)"""

#loop - square

"""for steps in range(4):
    turtle.forward(100)
    turtle.right(90)"""

#indented code is repeated
"""for steps in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.color('blue')
turtle.forward(200)"""

#nested loop 1
"""for anyname in range(4):
    turtle.forward(100)
    turtle.right(90)
    for moresteps in range(4):
        turtle.forward(50)
        turtle.right(90)"""

#nested loop 2
"""sides = 10
for steps in range(sides):
    turtle.forward(100)
    turtle.left(360/sides)
    for moresteps in range(sides):
        turtle.forward(50)
        turtle.left(360/sides)"""

#skip values by specifying a step 
#(min,max, step jump)

"""for steps in range(1, 10, 2):
    print(steps)"""

#tell which values to use in the loop

"""for clr in ['red', 'blue', 'yellow', 'brown', 'grey'] : 
    turtle.color(clr)
    turtle.forward(100)
    turtle.right(90)"""




