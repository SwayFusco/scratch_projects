"""
Author:  Sway (bryant) Fusco
Project: Week 3 Technical Assignment
Version: 20231218-231533
Cohort:  2023-11-30-de-eastern
Teacher: Tiago Basil
School:  Promineo Tech/ACC Data Engineering
"""
print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's Play! :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphical processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does UPS stand for? ")
if answer.lower() == "universal power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

print("You got " + str(score) + " question(s) correct!")
print("You got " + str((score / 4) * 100) + "%.")