# challenge-1
# average height calculator
# student_heights=input("enter heights\n").split();
# sum=0
# for n in range(0,len(student_heights)):
#     student_heights[n] =int( student_heights[n])
#     sum+=student_heights[n]
# avg= round(sum/len(student_heights)  )  
# print(avg)


# challenge-2
# figure out the heighest number 

# student_heights=input("enter heights\n").split();
# for n in range(0,len(student_heights)):
#     student_heights[n] =int( student_heights[n])
# highestScore=0
# for score in student_heights:
#     if(score >highestScore):
#        highestScore=score 
# print(f"the highest score is {highestScore}")

# num=int(input("enter the number of between 0 and 1000\n"))
# sum=0
# for n in range(0,num+1,2):
#     sum+=n
# print(f"the sum even number 0 and {num} is {sum}")


# challenge-3
# FizzBuzz change
for i in range(1,101):
    if(i%3==0 and i%5==0):
        print(f"Fizz Buzz")
    elif(i%3==0):
        print(f"Fizz")
    elif(i%5==0):
        print(f"Buzz")
    else:
            print(i)

    
    
