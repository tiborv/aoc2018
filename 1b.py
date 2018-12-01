import sys
values=[int(x) for x in sys.stdin.readlines()]
seen, sum, i = set([0]), 0, 0

while True:
    sum += int(values[i % len(values)])
    if sum in seen:
        print(sum)
        break
    seen.add(sum)
    i+=1