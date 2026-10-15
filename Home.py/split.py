numbers = input("Enter numbers separated by space: ").split()

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("Original list =", numbers)
print("Unique list =", unique)