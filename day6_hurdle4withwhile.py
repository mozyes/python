#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turning_right():
    turn_right()
    move()
    turn_right()
    move()
    
while not at_goal():
    if wall_in_front():
        turn_left()
        while wall_on_right():
            move()
        turning_right()
        while wall_on_right() and not wall_in_front():
            move()
        turn_left()
    elif front_is_clear():
        move()    
