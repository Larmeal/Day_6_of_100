# on http://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# From me : manual version

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while at_goal() != True:
#     if front_is_clear() == True:
#         move()
#         turn_right()
#         if front_is_clear() == True:
#             move()
#             turn_right()
#         elif wall_in_front() == True:
#             turn_left()
#             if wall_in_front() == True:
#                     turn_left()
#     elif wall_in_front() == True:
#         turn_left()
#         if front_is_clear() == True:
#             move()
#             turn_right()

# From me : upgrade version

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def walk ():
#     while wall_in_front() == True:
#         turn_left()
#     while wall_on_right() == True:
#         if front_is_clear() == True:
#             move()
#         elif wall_in_front() == True:
#             turn_left()
        
#     turn_right()
#     move()
#     turn_right()
        
# while at_goal() != True:
#     if front_is_clear() == True:
#         move()
#     elif wall_in_front() == True:
#         walk()

#เจอบัคไม่ยอมจบตอนถึงเส้นชัย

# #New version

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def walk ():
#     while wall_in_front() == True:
#         turn_left()
#     while wall_on_right() == True and wall_on_right() != at_goal():
#         if front_is_clear() == True:
#             move()
#         elif wall_in_front() == True:
#             turn_left()
        
#     turn_right()
#     move()
#     turn_right()
        
# while at_goal() != True:
#     if front_is_clear() == True:
#         move()
#     elif wall_in_front() == True:
#         walk()

# #New version again

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while at_goal() != True:
#     if front_is_clear() == True:
#         if wall_on_right() != True:
#             turn_right()
#             move()
#             turn_right()
#             move()
#         else:
#             move()
#     elif wall_in_front() == True:
#         turn_left()
   
            
                
        
   
            
                
        