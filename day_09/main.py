# programming_dictionary={
#     "Bug":"An error in a program that prevents the program from running as expected.",
#     "Function":"A piece of code that you can easily call over and over again.",
# }

# # Retrieving items from dictionary
# # print(programming_dictionary["Bug"])

# # Adding new items to dictionary
# programming_dictionary["Loop"]="The action of doing something over and over again."


student_scores={
    "Harry":81,
    "Ron":78,
    "Hermonie":99,
    "Draco":74,
    "Neville":62
}

score_details={}
for key in student_scores:
    if student_scores[key] >=90 and  student_scores[key] <99:
        score_details[key]="Outstanding"
    elif(student_scores[key] >=80 and student_scores[key] <90):
        score_details[key]="Exceeds Expectations"
    elif(student_scores[key] >=70 and student_scores[key] <80):
        score_details[key]="Acceptable"
    elif(student_scores[key] >=60 and student_scores[key] <70):
        score_details[key]="Fail"
    
print ("Score Details: ",score_details)

