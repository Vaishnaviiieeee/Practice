# Meaningfull words from NAME 
Name = (input("Enter your name:"))
print("Meaningful words from your name:")
for word in Name.split():
    if len(word) > 8:
        print(word)
