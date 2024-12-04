list1 = []
list2 = []

with open('input.txt', 'r') as file:
    for line in file:
        values = line.split()
        list1.append(int(values[0]))
        list2.append(int(values[1]))

simularity_score = 0
for entry in list1:
    simularity_score += entry * list2.count(entry)

print(f'The answer is: {simularity_score}')