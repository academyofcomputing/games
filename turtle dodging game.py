import turtle as t
import random as r
import time

# Move the player left
def move_left():
    x = player.xcor()
    x -= 20
    if x < -400:
        x = -400
    player.setx(x)

# Move the player right
def move_right():
    x = player.xcor()
    x += 20
    if x > 400:
        x = 400
    player.setx(x)

# Collision detection function
def is_collision(t1, t2):
    return t1.distance(t2) < 20

def game_over():
    t.color('red')
    t.goto(0, 0)
    t.write("Game Over", align = 'center', font=("Berlin Sans FB Demi", 30, 'bold'))
    t.goto(0, -50)
    t.write("Click to Exit", align='center', font=("Berlin Sans FB Demi", 30, 'bold'))

# Set up the screen
wn = t.Screen()
wn.setup(width=800, height=800)
wn.bgcolor('black')
wn.title('Turtle Dodging Game')
wn.tracer(0) #turns off automatic screen update; screen update is done in the while loop


# Player (the turtle)
player = t.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.goto(0, -250)

# Obstacles
colors = ['red', 'green', 'orange', 'blue', 'yellow', 'white', 'purple']
shapes = ['circle', 'triangle', 'square']
balls = []


for i in range(10):  # create 5 obstacles
    ball = t.Turtle()

    ### pick a random shape
    random_shape = r.choice(shapes)
    ball.shape(random_shape) #t.shape('circle')

    ### pick a random color
    random_colors = r.choice(colors)
    ball.color(random_colors) #t.color('red')

    ball.shape(random_shape)
    ball.color(random_colors)
    ball.penup()
    ball.goto(r.randint(-400, 400), r.randint(-400, 400))
    balls.append(ball)


# Keyboard controls
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")


# Game loop
gameOver = False


while not gameOver:
    wn.update()
    # Move the obstacles
    for ball in balls:
        y = ball.ycor()
        y -= r.randint(5, 15)  # Move  downwards at random speeds
        ball.sety(y)

        # If the obstacle goes off the screen, reset its position
        if y < -400:
            ball.goto(r.randint(-400, 400), r.randint(200, 400))

        # Check for collision with the player
        if is_collision(player, ball):
            gameOver = True
            game_over()
            t.exitonclick()

    time.sleep(0.02)  # Slow down the loop
