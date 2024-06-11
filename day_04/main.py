# import random
# c=random.randint(100,300)
# print(c)

# challenge-1
# Tail or Head Game

# import random
# number= random.randint(0,1)
# if(number==1):
#     print("Head")
# else:
#     print("Tail")


# challenge-2
# select the man who pays the bill
# print("Who pay the bill?\n")
# import random
# names_string= input("write your name by separating in comma\n")

# names=names_string.split(",")
# length= len(names)
# index=random.randint(0, length-1)
# selected_name=names[index]


# print(f"{selected_name} is going to pay the bill today?\n")

# challenge-3
# treasure map
# line1=["*","*","*"]
# line2=["*","*","*"]
# line3=["*","*","*"]

# map=[line1,line2,line3]
# print("Hidding your Treasures in a map, O marks the spot")
# position=  input("Where do you want to put your Treasures?\n")
# letter=position[0].lower()
# abc=["a", "b", "c"]
# letter_index=abc.index(letter)
# number_index=int(position[1])-1
    
# map[number_index][letter_index]="O"


# print(f"{line1}\n{line2}\n{line3}\n")
