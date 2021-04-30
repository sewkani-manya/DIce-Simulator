#dice.py
import random

min = 1
max=6

roll = input("Roll the dice yes/no?")

while roll=="yes" or roll=="y":
    print ("The value is  ")
    print (random.randint(min,max))
    roll =  input ("Roll the dice again?")
