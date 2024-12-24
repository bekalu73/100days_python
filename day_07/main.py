# step1
import random
# word_list = ["ardvark", "baboon", "camel"]
# randNum=random.randint(0,len(word_list)-1)
# chosen_word=word_list[randNum]
# gusess= input("please guess letter\n").lower()
# # make the list from guess letters
# choosen_list=chosen_word.split(',')
# print("choosen word",chosen_word)
# for i in range(len(choosen_list)):
#     if(i==gusess):
#         print(f"you guessed letter correctly")
#     else:
#         print(f"you guessed wrong letter ")


# step2
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
guess = input("Please guess a letter: \n").lower()
print(f"Chosen word: {chosen_word}")

display_list = ["_" for _ in chosen_word]

for index, letter in enumerate(chosen_word):
    if letter == guess:
        display_list[index] = letter

print(f"Updated display: {' '.join(display_list)}")

