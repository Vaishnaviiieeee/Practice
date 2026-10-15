# Q6. Reverse the list
n = int(input("Enter Number of elements in list: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Element {i + 1}: ")))
print("Original list:", arr)
arr.reverse()
print("Reversed list:", arr)