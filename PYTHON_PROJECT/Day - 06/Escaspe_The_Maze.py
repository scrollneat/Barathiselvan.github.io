# Reeborg's World
# https://reeborg.ca/
def turn_right():
    turn_left()
    turn_left()
    turn_left()
#start
def hurdle_clear():
    turn_right()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
while front_is_clear():
    move()
while not at_goal():
        if right_is_clear():
            turn_right()
            while front_is_clear():
                move()
        elif front_is_clear():
            while front_is_clear():
                move()
        else:
            turn_left()
            
            
