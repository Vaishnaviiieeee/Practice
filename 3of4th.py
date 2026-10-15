# insert a item or insert a number in a list at 6th position this number must be one third of number stored at 4th position
N = input("Enter the number of elements in the list: ")
N = int(N)  
list1 = []
for i in range(N):
    element = int(input(f"Enter element {i+1}: "))
    list1.append(element)
print("The list is:", list1)
if N >= 4:
    number_to_insert = list1[3] // 3  # One third of the number at 4th position 
    if N >= 6:
        list1.insert(5, number_to_insert)  # Insert at 6th position 
    else:
        list1.append(number_to_insert)  # If less than 6 elements, append to the end
    print("The updated list is:", list1)