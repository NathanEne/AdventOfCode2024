import re
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
running_sum = 0
with open('input.txt', 'r') as corrupted_memory :
    for line in corrupted_memory:
        matches = re.findall(pattern, line)
        running_sum += sum(int(x) * int(y) for x, y in matches)
print(f'The answer is: {running_sum}')