# Q2. Square of first N numbers starting form S
S = int(input("Enter your number S:"))
N = int(input("Enter your number N:"))
sum = 0
for i in range(1, N + 1):
    square = i * i
    sum += square
print("The sum of squares of first N numbers is:", sum)