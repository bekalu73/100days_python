import random


RandNumber = random.randint(1,100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty= input("Choose a difficulty. Type 'easy' or 'hard':\n")
if difficulty=="easy":
    attempts=10
else:
    attempts=5

print(f"You have {attempts} attempts remaining to guess the number.")

while attempts>0:
    guess= int(input("Make a guess: "))
    if guess==RandNumber:
        print(f"You got it! The answer was {RandNumber}")
        break
    elif guess<RandNumber:
        print("Too Low")
    else:
        print("Too High")
    attempts-=1
    print(f"You have {attempts} attempts remaining to guess the number.")
    if attempts==0:
        print(f"You've run out of guesses, you lose. The number was {RandNumber}")
        break
    else:
        print("Guess again.")
