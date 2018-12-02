import sys

two, three = 0, 0
for line in sys.stdin:
    chars = set(list(line.strip()))
    vals = [line.count(chr) for chr in chars]
    two += 1 if 2 in vals else 0
    three += 1 if 3 in vals else 0

print(two*three)