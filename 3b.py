import sys

fabric = [['.' for i in xrange(1000)] for j in xrange(1000)]
hasOverlaps = set()

def mark(x, y, val, fabric):
    if fabric[y][x] == '.':
        fabric[y][x] = val
        return fabric
    hasOverlaps.update([val, fabric[y][x]])
    fabric[y][x] = 'X'
    return fabric

def markArea(x, y, xs, ys, val, fabric):
    for i in xrange(xs):
        for j in xrange(ys):
            fabric = mark(x+i, y+j, val, fabric)
    return fabric

maxId = 0
for line in sys.stdin:
    info = line.replace(':', '').split()
    id = info[0].split('#')[1]
    if int(id) > maxId: maxId = int(id)
    x, y = info[2].split(',')
    xs, ys = info[3].split('x')
    fabric = markArea(int(x), int(y), int(xs), int(ys), id, fabric)

def findNoOverlaps(max, overlaps):
    for i in xrange(1, max):
        if str(i) not in overlaps:
            return i

print(findNoOverlaps(maxId, hasOverlaps))