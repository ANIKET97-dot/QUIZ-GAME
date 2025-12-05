# QUIZ GAME
print("Hi Guys, Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "Central Processing Unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Central Processing Unit.")
    

answer = input("What does ATM stands for? ")
if answer.lower() == "Automatic Tailor Machine":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Automatic Tailor Machine.")
    

answer = input("What does RAM stand for? ")
if answer.lower() == "Random Access Memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Random Access Memory.")
    

answer = input("What does PSU stand for? ")
if answer.lower() == "Power Supply Unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Power Supply Unit.")
print("Thanks for playing!")

print("Your final score is " + str(score) + " out of 4.")
print("You got " + str((score / 4) * 100) + "%.")
