# Q4. Count vowels and its count
S = input("Enter your sentence: ")
vowels = 0
if S:   
    for i in S:
        if i in "aeiouAEIOU":
            vowels += 1
            count = vowels
print("Number of vowels:", vowels)
print("Number of a or A's:", S.count('a') + S.count('A'))
print("Number of e or E's:", S.count('e') + S.count('E'))
print("Number of i or I's:", S.count('i') + S.count('I'))
print("Number of o or O's:", S.count('o') + S.count('O'))
print("Number of u or U's:", S.count('u') + S.count('U'))
