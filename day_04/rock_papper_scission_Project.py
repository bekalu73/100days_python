print("Rock Paper Scissior Application")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
userInp= int(input("What do You Choose? Type 0 for rock, 1 for papper, 2 for Scissior"))
gameArr=[rock,paper,scissors];
RandNum= random.randint(0,2)
userChoice= gameArr[userInp]
machineChoice= gameArr[RandNum]    
if(userChoice=="rock" and machineChoice=="paper"):
    print(f"your Choice\n{userChoice}")
    print(f"machine Choice\n{machineChoice}")
    print(f"you win")
elif(userChoice=="paper" and machineChoice=="rock"):
    print(f"your Choice\n{userChoice}")
    print(f"machine Choice\n{machineChoice}")
    print("you win")
elif(userChoice=="scissiors" and machineChoice=="paper"):
    print(f"your Choice\n{userChoice}")
    print(f"machine Choice\n{machineChoice}")
    print("you win")
else:
    print(f"your Choice\n{userChoice}")
    print(f"machine Choice\n{machineChoice}")
    print("Machine win")
