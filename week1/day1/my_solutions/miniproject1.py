import random
import math


secret_num = random.randint(0,10)
guess_num = int(input("Guess the number"))


def compare(secret_num,guess_num):
    if(secret_num==guess_num):
        print("Player wins and computer loose")
    else:
        print("Computer wins and player loose")


print("ajhd")