#rockpaperscissors.py

import random

user_action=input(" Choose one(rock, paper, scissors:)")
possible_action=(rock,paper,scissors)
comp_action=random.randit(possible_action)
print("you chose", user_action, "the computer chose", comp_action)

if user_action==comp_action:
    print("you both chose", user_action,"Tie")
elif user_action=="paper":
    if comp_action=="rock":
        print("you win")
    else:
        print("computer wins")
elif user_action=="rock":
    if comp_action=="scissors":
        print("you win")
    else:
        print("computer wins")
elif user_action=="scissors":
    if comp_action=="paper":
        print("you win")
    else:
        print("computer wins")
