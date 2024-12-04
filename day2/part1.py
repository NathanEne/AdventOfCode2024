safe_report_count = 0

with open('input.txt', 'r') as file:
    for line in file:
        list = line.split()
        list_int = [int(item) for item in list]
        differences = [list_int[i+1] - list_int[i] for i in range(len(list_int) - 1)]
        if all(-3 <= difference <= -1 for difference in differences) or all(1 <= difference <= 3 for difference in differences):
            safe_report_count += 1


print(f'The answer is: {safe_report_count}')