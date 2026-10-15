# Sum of first 10 numbers
n = int(input("Enter your number:"))
sum = 0
i = 0
while i < n:
    if i % 2 == 0:
        sum += i
    i += 1
print("The sum of even numbers is:", sum)