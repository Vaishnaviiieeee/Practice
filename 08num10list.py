# create a list of 10 numbers
N = 10
list1 = []
for i in range(N):
    element = int(input(f"Enter element {i+1}: "))
    list1.append(element)
print("The list is:", list1)