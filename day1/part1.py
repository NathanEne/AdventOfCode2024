list1 = []
list2 = []

with open('input.txt', 'r') as file:
    for line in file:
        values = line.split()
        list1.append(int(values[0]))
        list2.append(int(values[1]))

list1.sort()
list2.sort()

running_total = 0
for entry1, entry2 in zip(list1, list2):
    running_total += abs(entry1 - entry2)

print(f'The answer is: {running_total}')