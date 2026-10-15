# Q5 remove duplicates
n = int(input("Enter your Element number: "))
arr = []

for i in range(n):
    arr.append(int(input(f"Element {i + 1}: ")))
unique = []

for num in arr:
    if num not in unique:
        unique.append(num)

print("Original:", arr)
print("Removed duplicates:", unique)
