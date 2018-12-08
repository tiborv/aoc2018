import sys

inpt = [(int(line.split(",")[0]), int(line.split(",")[1].strip())) for line in sys.stdin.readlines()]

def dist(a, b):
    return  abs(a[0] - b[0]) + abs(a[1] - b[1])

def fillArea(area, points):
    tx, ty = area
    res = [['' for zz in xrange(tx)] for aa in xrange(ty)]
    for y in xrange(ty):
        for x in xrange(tx):
            dists = [dist((x, y), p) for p in points]
            res[y][x] = '#' if sum(dists) < 10000 else '.'
    return res


fill = fillArea((400, 400), inpt)

def countFill(fill):
    c = 0
    for y in xrange(len(fill)):
        c+= fill[y].count('#')
    return c

print(countFill(fill))


    