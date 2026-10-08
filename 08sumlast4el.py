# print a sum of last 4 elements of the list
N = input("Enter the number of elements in the list: ")
N = int(N)
list1 = []
for i  in range(N):
    element = int(input(f"Enter element {i+1}: "))
    list1.append(element)
print("The list is:", list1)
sum_of_last_4 = sum(list1[-4:])
print("The sum of the last 4 elements is:", sum_of_last_4)