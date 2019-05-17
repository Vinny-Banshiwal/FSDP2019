import random
import math
guess_left=0
secret_num=0


def guessnumber():
    secret_num = random.randint(0,10)
    guess_num = int(input("Guess the number"))

    