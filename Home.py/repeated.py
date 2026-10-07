numbers = input("Enter numbers separated by space: ").split()

found = False

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            print("First repeated element =", numbers[i])
            found = True
            break

    if found:
        break

if found == False:
    print("No repeated element found")