"""
Cretor: Elderny
Editor: Elderny
Date: 1/06/2021
purpose: Practice
"""
import pygame
from pygame import mixer

# for creating time gaps between functions
import time

# for randomizing our winning number
import random
print("\nWelcome to the guess the Number Game, made by @elderny1 from telegram!\n")

# for asking if user wants help or not!
ask = int(input("To start the Game Press '1', to know more about the game Press '2' \nType Here: "))
if ask == 1:
    pass
elif ask == 2:
    print(f"\nInstructions: You need to fill names for both players you are your opponent,\n"
          f"Then you need to put any two numbers. First Number should be smaller and Last Number should be greater!"
          f", \nThen you need to guess any number that is available in between the numbers you provided, "
          f"as the winning number would be randomly selected!"
          f". \nThe Person who would choose the number with wasting less trials will win!\n")
    print("STARTING GAME IN 5 SECS...")
    time.sleep(5)

# Background Music
mixer.init()
mixer.music.load("background.mp3")
mixer.music.play(-1)

# This will collect guessing number range
def asking_number():
    while True:
        print(f"You need to type two numbers. First Smaller, Second Greater")
        number_a = int(input("Type First Number \nType here: "))
        time.sleep(0.5)
        print(f"Registered First number as {number_a}\n")
        number_b = int(input("Type Second Number \nType here: "))
        time.sleep(0.5)
        print(f"Registered Last number as {number_b}\n")
        numc = [number_a, number_b]

        if number_a < number_b:
            return numc
        elif number_a == number_b:
            print("Error: both numbers detected as equal\n")
        elif number_a > number_b:
            print("Error: first number is larger then last number\n")
        else:
            print("Unknown Value\n")

# This will collect names for players
def names():
    print("\nHey Players! Type your Names")
    name_1 = input("Type the Player1 Name \nName: ")
    time.sleep(0.5)
    print(f"Saved Player1 Name as {name_1}\n")
    name_2 = input("Type the Player2 Name \nName: ")
    time.sleep(0.5)
    print(f"Saved Player2 Name as {name_2}")
    name_list = [name_1, name_2]
    return name_list

# It will allocate names to Player functions
name_manager = names()

def player1():
    trials = 0
    print(f"{name_manager[0]} is Playing as Player1, Starting the Game")
    time.sleep(1)
    print(f"Game Started!\n")
    winning_number = asking_number()
    randomer = random.randint(winning_number[0], winning_number[1])
    while True:
        num_guesser = int(input("Guess any number between Your specified numbers: \nType here: "))
        trials += 1
        if num_guesser == randomer:
            print("Yup that's correct!")
            print(f"It took You {trials} trials, to guess the Correct number")
            return trials
        elif num_guesser > randomer:
            print(f"Wrong guess, the correct number is Smaller then {num_guesser}")
        elif num_guesser < randomer:
            print(f"Wrong guess, correct number is Greater then {num_guesser}")

def player2():
    trials = 0
    print(f"{name_manager[1]} is playing as Player2, Starting the Game")
    time.sleep(1)
    print(f"Game Started!\n")
    winning_number = asking_number()
    randomer = random.randint(winning_number[0], winning_number[1])
    while True:
        num_guesser = int(input("Guess any number between Your specified numbers: \nType here: "))
        trials += 1
        if num_guesser == randomer:
            print("Yup that's correct!")
            print(f"It took You {trials} trials, to guess the Correct number")
            return trials
        elif num_guesser > randomer:
            print(f"Wrong guess, the correct number is Smaller then {num_guesser}")
        elif num_guesser < randomer:
            print(f"Wrong guess, correct number is Greater then {num_guesser}")

#Playing Game as Player1 and Player2
def playing():
    while True:
        print(f"\n--------Player 1 {name_manager[0]} Turn--------\n")
        play1 = player1()
        print(f"\n--------Player 2 {name_manager[1]} Turn--------\n")
        play2 = player2()
        if play1 < play2:
            print(f"\n------Player1 {name_manager[0]}, Won!------\n")
        elif play1 > play2:
            print(f"\n------Player2 {name_manager[1]}, Won!------\n")
        elif play1 == play2:
            print("Draw Match")
        ask = int(input("Want to Play Again?, Type '1' if Yes or '2' if No: "))
        if ask == 1:
            pass
        elif ask == 2:
            print("Exiting The Program!")
            exit()
        else:
            print("Unknown command, starting New Game")

# Calling playing Function
starting = playing()