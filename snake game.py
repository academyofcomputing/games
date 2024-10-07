Skip to content
 
Search Gists
Search...
All gists
Back to GitHub
@academyofcomputing
academyofcomputing/snake game Secret
Created 4 months ago
Code
Revisions
1
Clone this repository at &lt;script src=&quot;https://gist.github.com/academyofcomputing/f1c4d041185256c54a093cdc2d14308b.js&quot;&gt;&lt;/script&gt;
<script src="https://gist.github.com/academyofcomputing/f1c4d041185256c54a093cdc2d14308b.js"></script>
snake game
#################################
# initialization
#################################
import turtle as t
import time
import random

#screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
wn = t.Screen()
wn.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
wn.bgcolor('black')
wn.title('Snake Game')
wn.tracer(0)


# Snake head
head = t.Turtle()
head.speed(0) #set animation speed to highest
head.shape("circle")
head.color("grey")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake body
body = []

### exercise: create the food with red color, circle shape at location (100, 100)

# food
food = t.Turtle()
food.speed(0) #set animation speed to highest
food.shape("circle")
food.color("red")
food.penup()
x = random.randint(-SCREEN_WIDTH//2+20, SCREEN_WIDTH//2-20)
y = random.randint(-SCREEN_HEIGHT//2+20, SCREEN_HEIGHT//2-20)
food.goto(x, y)

# Score
score = 0
high_score = 0
pen = t.Turtle()
pen.speed(0)
pen.color("white") #need to set color otherwise the score will be written in black, not visible on black screen
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "bold"))

delay = 0.1



#################################
# function
#################################

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def head_move():
    if head.direction == "up":
        y = head.ycor() #y-coordinate (50, 100)
        head.sety(y + 10)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 10)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 10)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 10)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")



# ###################################
# # # # while loop for game logic
# ###################################

while True:

    wn.update()

    # stop the snake when it hits the wall
    if head.xcor() > SCREEN_WIDTH//2 or head.xcor() < -SCREEN_WIDTH//2 or head.ycor() > SCREEN_HEIGHT//2 or head.ycor() < -SCREEN_HEIGHT//2:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for segment in body:
            segment.goto(SCREEN_WIDTH+200, SCREEN_HEIGHT+200)
        body.clear()

        # Reset the score
        score = 0

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


    # check if snake eats food
    if head.distance(food) < 20:
        x = random.randint(-SCREEN_WIDTH // 2 + 20, SCREEN_WIDTH // 2 - 20)
        y = random.randint(-SCREEN_HEIGHT // 2 + 20, SCREEN_HEIGHT // 2 - 20)
        food.goto(x, y)

        # Add a segment
        body_seg = t.Turtle()
        body_seg.speed(0)
        body_seg.shape("square")

        body_seg.color("green")
        body_seg.penup()
        body.append(body_seg)

        # Increase the score
        score = score + 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


    # Move the end segments first in reverse order
    for index in range(len(body) - 1, 0, - 1):
        # print("inside for loop")
        # print(index)
        x = body[index - 1].xcor()
        y = body[index - 1].ycor()
        body[index].goto(x, y)

    # move segment 0 to where the head is
    if len(body) > 0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x, y)

    head_move()
    time.sleep(delay)
@academyofcomputing
Comment
 
Leave a comment
 
Footer
© 2024 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact
Manage cookies
Do not share my personal information
snake game
