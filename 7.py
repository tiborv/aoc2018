import sys

steps = {}
allSteps = set()
for line in sys.stdin:
    step = line.split()
    steps[step[7]] = steps[step[7]] | set(step[1]) if step[7] in steps else set(step[1])
    allSteps.add(step[7])
    allSteps.add(step[1])

seq = sorted(allSteps)
done = set()
order = []
while seq:
    for i, c in enumerate(seq):
        if c not in steps or len(steps[c] - done) == 0:
            order.append(c)
            done.add(c)
            del seq[i]
            break
print("".join(order))