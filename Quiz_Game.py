print("Welcome TO Quiz Game")

player_name = input("Enter Your Name: ")

print(f"Hello, {player_name}")

playing = input("Do you want to proceed(Yes/No): ").lower()

if playing != "yes":
    quit("Good Bye")

else:
    print("Let's Play!")

score = 0

answer = input("Who is the Father of the Computer? ").lower()
if answer == "charles babbage":
    print("Correct!")
    score += 10
else:
    print("Incorrect")

answer = input("What is the full form of RAM?: ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 10
else:
    print("Incorrect")

answer = input("RAM is a ______________ memory. ").lower()
if answer == "volatile":
    print("Correct!")
    score += 10
else:
    print("Incorrect")

answer = input("Who invented Compact Disc? ").lower()
if answer == "james russell":
    print("Correct!")
    score += 10
else:
    print("Incorrect")

answer = input("CPU stands for _____________. ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 10
else:
    print("Incorrect")

answer = input("What does ROM stand for? ").lower()
if answer == "read only memory":
    print("Correct!")
    score += 10
else:
    print("Incorrect")

answer = input("How much is a byte equal to bits: ").lower()
if answer == "8" or "8 bits":
    print("Correct!")
    score += 10
else:
    print("Incorrect")

answer = input("WWW stands for ____________. ").lower()
if answer == "world wide web":
    print("Correct!")
    score += 10
else:
    print("Incorrect")

answer = input("What is the full form of E-Mail? ").lower()
if answer == "electronic mail":
    print("Correct!")
    score += 10
else:
    print("Incorrect")

answer = input("A computer is a/ an _____________ device. ").lower()
if answer == "electronic":
    print("Correct!")
    score += 10
else:
    print("Incorrect")


print("\nQuiz End")

if score > 50:
    print(f"\nCongratulation you scored {score}% in Quiz Game.")

elif score < 50:
    print(f"\nYou scored {score}% in quiz game. Better Luck Next Time")
