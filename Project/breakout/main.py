import turtle

# Set up the screen
window = turtle.Screen()
window.title("Breakout Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Bricks
bricks = []

# Create bricks
for _ in range(5):
    for _ in range(10):
        brick = turtle.Turtle()
        brick.speed(0)
        brick.shape("square")
        brick.color("white")
        brick.penup()
        brick.goto(-360 + 80 * _, 200 - 20 * _)
        bricks.append(brick)

# Functions to move the paddle left and right
def paddle_right():
    x = paddle.xcor()
    x += 20
    if x < 360:  # Limit the paddle's movement within the window
        paddle.setx(x)

def paddle_left():
    x = paddle.xcor()
    x -= 20
    if x > -360:  # Limit the paddle's movement within the window
        paddle.setx(x)

# Keyboard bindings
window.listen()
window.onkeypress(paddle_right, "Right")
window.onkeypress(paddle_left, "Left")

# Update function for the game loop
def update():
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1

    # Paddle and ball collisions
    if (ball.ycor() > -240) and (ball.ycor() < -230) and (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        ball.sety(-230)
        ball.dy *= -1

    # Ball and brick collisions
    for brick in bricks:
        if brick.distance(ball) < 20:
            brick.hideturtle()
            bricks.remove(brick)
            ball.dy *= -1

    # Check for a win
    if len(bricks) == 0:
        win_text = turtle.Turtle()
        win_text.speed(0)
        win_text.color("white")
        win_text.penup()
        win_text.hideturtle()
        win_text.goto(0, 0)
        win_text.write("Congratulations! You win!", align="center", font=("Courier", 24, "normal"))

    # Call the update function after a delay
    window.ontimer(update, 10)  # Adjust the delay to control the game speed

# Start the game loop
update()

# Close the window on click
window.exitonclick()
