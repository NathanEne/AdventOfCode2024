safe_report_count = 0

with open('input.txt', 'r') as file:
    for line in file:
        list = line.split()
        list_int = [int(item) for item in list]
        for i in range(len(list_int)):
            silced_list = list_int[:i] + list_int[i+1:]
            differences = [silced_list[i+1] - silced_list[i] for i in range(len(silced_list) - 1)]
            if all(-3 <= difference <= -1 for difference in differences) or all(1 <= difference <= 3 for difference in differences):
                safe_report_count += 1
                break


print(f'The answer is: {safe_report_count}')