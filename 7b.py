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

time = lambda c: ord(c) - 4
sec = 0
workers = ['.', '.', '.', '.', '.']
willFinish = {}
finished = set()
while True:
    if sec in willFinish:
        for o in willFinish[sec]:
            if o in order:
                order.remove(o)
            finished.add(o)
        workers = map(lambda o: '.' if o in willFinish[sec] else o, workers)
        del willFinish[sec]

    for i, w in enumerate(workers):
        if w == '.':
            for o in order:
                if '.' not in workers:
                    break
                if o not in workers and not len(set(steps[o] if o in steps else []) - finished) > 0:
                    workers[i] = o
                    finsec = sec + time(o)
                    if finsec in willFinish:
                        willFinish[finsec].append(o)
                    else:
                        willFinish[finsec] = [o]
    if workers.count('.') == len(workers):
        break
    sec += 1


print(sec)
  


