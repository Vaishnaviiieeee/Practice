# Q7 star pyramid of 3 rows
print("3 star pyramid")
i = int(input("Enter the number of rows: "))
for i in range(1, i + 1):
    print(""*(i-i), end="")

    if i == 1:
        print("*"*i)
    elif i == 2:
        print("+"*i)
    elif i == 3:
        print("*"*i)


  

   

