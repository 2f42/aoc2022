from itertools import takewhile


with open("input.txt") as f:
    calories = [0, 0, 0]
    running_total = 0
    for line in f:
        if line.strip() == "":
            if running_total > min(calories):
                calories.remove(min(calories))
                calories.append(running_total)
            running_total = 0
            continue
        running_total += int(line.strip())
    print(calories)
    print(sum(calories))

