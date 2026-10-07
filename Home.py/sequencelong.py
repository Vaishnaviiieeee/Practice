numbers = [100, 4, 200, 1, 3, 2]

longest_sequence = []
current_sequence = []

for num in numbers:
    current_sequence = [num]

    next_num = num + 1

    while next_num in numbers:
        current_sequence.append(next_num)
        next_num = next_num + 1

    if len(current_sequence) > len(longest_sequence):
        longest_sequence = current_sequence

print("Longest consecutive sequence =", longest_sequence)
print("Length =", len(longest_sequence))