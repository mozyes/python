def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

Number_of_hurdles = 6
i = 0
while i < 6:
    i += 1
    jump()
