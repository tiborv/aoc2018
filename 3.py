import sys

fabric = [['.' for i in xrange(1000)] for j in xrange(1000)]

def mark(x, y, val, fabric):
    fabric[y][x] = val if fabric[y][x] == '.' else 'X'
    return fabric

def markArea(x, y, xs, ys, val, fabric):
    for i in xrange(xs):
        for j in xrange(ys):
            fabric = mark(x+i, y+j, val, fabric)
    return fabric

for line in sys.stdin:
    info = line.replace(':', '').split()
    id = info[0].split('#')[1]
    x, y = info[2].split(',')
    xs, ys = info[3].split('x')
    fabric = markArea(int(x), int(y), int(xs), int(ys), id, fabric)

countX = lambda fabric: sum([fabric[i].count('X') for i in xrange(len(fabric))])

print(countX(fabric))
