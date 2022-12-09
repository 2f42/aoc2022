
with open("input.txt") as f:
    overlaps_entirely = []
    overlaps = []
    for line in f:
        split = [list(map(int, x.split("-"))) for x in line.split(",")]
        max_range = [min(split[0][0], split[1][0]), max(split[0][1], split[1][1])]
        min_range = [max(split[0][0], split[1][0]), min(split[0][1], split[1][1])]
        if max_range in split:
            overlaps_entirely.append(line.strip())
        if min_range[0] <= min_range[1]:
            overlaps.append(line.split())
    print(len(overlaps_entirely))
    print(len(overlaps))
