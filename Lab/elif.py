# X = int(input("Enter value"))
# if X > 0:
#     print("Positive")
# elif X == 0:
#     print("Zero") 
# else:
#     print("Negitive")  
# 
# print("Output of while loop")
# count = 0
# while count <5:
#     print(count)
#     count +=1     

# For loop
# print("print for loop")
# for i in range(5):
#     print(i)

# CREATE DICTIONARY WITH STUDENT DETAILS
Students = {
    101:{"Name":"Aditi", "scores": [78,85,90]},
    102:{"Name":"Navya", "scores": [78,86,48]},
    103:{"Name":"Preeti", "scores": [68,37,70]},
    104:{"Name":"Reshma", "scores": [94,94,50]},
    105:{"Name":"Tarun", "scores": [63,65,85]},
}
# CALCULATE AVERAGE SCORE OF EACH STUDENT
for student_id, details in Students.items():
    avg = sum(details["scores"]) / len(details["scores"])
    details["Average"] = avg
    details["passed"] = avg >= 50         # BOOLEAN FLAG

# PRINT NAMES OF STUDENTS WHO PASSED
print("Students who passed:")
for student_id, details in Students.items():
    if details["passed"]:
        print(details["Name"])