
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open("input.txt") as f:
    total = 0
    lines = f.read().splitlines()
    for elf1, elf2, elf3 in zip(lines[0::3], lines[1::3], lines[2::3]):
        common = set(elf1).intersection(set(elf2)).intersection(set(elf3))
        total += 1 + alphabet.index(next(iter(common)))
    print(total)

