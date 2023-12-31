"""
Author:  Sway (bryant) Fusco
Project: Simple Quiz Game
Version: 20231231-141614
"""
# Welcome message
print("Welcome to my computer quiz!")

# Ask if the user wants to play
playing = input("Do you want to play? ")

# Check if the user wants to play, otherwise quit
if playing.lower() != "yes":
    quit()

# Inform that the game is starting
print("Okay! Let's Play! :)")
score = 0

# Question 1
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

# Question 2
answer = input("What does GPU stand for? ")
if answer.lower() == "graphical processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

# Question 3
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

# Question 4
answer = input("What does UPS stand for? ")
if answer.lower() == "universal power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

# Display the final score
print("You got " + str(score) + " question(s) correct!")
print("You got " + str((score / 4) * 100) + "%.")
