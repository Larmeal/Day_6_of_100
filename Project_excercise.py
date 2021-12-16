# พาหุ่นยนต์ไปเข้า เส้นชัน

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def walk():
    while wall_in_front() == True and at_goal != True:
        if wall_on_right() == True:
            turn_left()
        elif wall_on_right() != True:
            turn_right()
            move()
            
while at_goal != True:
    if front_is_clear() == True and at_goal != True:
        if front_is_clear() == True and right_is_clear() == True:
            turn_right()
            move()
        else:
            move()
    else: 
        walk()

