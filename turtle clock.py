# shape turtle
# multiple turtles
# draw a turtle clock showing 3pm

import turtle as t

# t1 = t.Turtle()
# t2 = t.Turtle()
#
# t1.shape('turtle')
# t2.shape('turtle')
# t1.color('red')
# t2.color('green')
# t1.forward(100)
# t2.backward(100)


# a turtle clock
t.bgcolor('black')
turtles = []
colors = ['red', 'green', 'yellow', 'blue', 'purple', 'white', 'cyan', 'orange', 'magenta', 'pink', 'wheat', 'tomato']
t.speed(0)

for i in range(12):
    next = t.Turtle()
    next.shape('turtle')
    next.color(colors[i])
    next.left(i*30)
    next.penup()
    next.forward(100)

t.goto(0, 0)
t.shape('circle')
t.color('white')
t.stamp()
t.pendown()
t.pensize(4)
t.goto(60, 0)
t.penup()
t.goto(0,0)
t.pendown()
t.pensize(2)
t.goto(0, 80)
t.hideturtle()
t.done()
