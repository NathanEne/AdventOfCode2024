import re
do_dont_mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"
running_sum = 0
enabled = True
with open('input.txt', 'r') as corrupted_memory :
    for line in corrupted_memory:
        for match in re.finditer(do_dont_mul_pattern, line):
            if match.group() == 'do()':
                enabled = True
            elif match.group() == "don't()":
                enabled = False
            else:
                if enabled:
                    x = match.group(1)
                    y = match.group(2)
                    running_sum += int(x) * int(y) 

print(f'The answer is: {running_sum}')