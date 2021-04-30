#rockpaperscissors.py
import random

user_action=input(" Choose one(rock, paper, scissors:)")
possible_action=(rock,paper,scissors)
comp_action=random.randit(possible_action)
print("you chose", user_action, "the computer chose", comp_action)
