# find out the difference between maximum and minimum element of the list
N = input("Enter the number of elements in the list: ")
N = int(N)
list1 = []
for i in range(N):
    element = int(input(f"Enter element {i+1}: "))
    list1.append(element)
print("The list is:", list1)
diff = max(list1) - min(list1)
print("The difference between the maximum and minimum elements is:", diff)