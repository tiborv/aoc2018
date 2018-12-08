import sys

inpt = [(int(line.split(",")[0]), int(line.split(",")[1].strip())) for line in sys.stdin.readlines()]

def dist(a, b):
    return  abs(a[0] - b[0]) + abs(a[1] - b[1])

def fillArea(area, points):
    tx, ty = area
    res = [['' for zz in xrange(tx)] for aa in xrange(ty)]
    for y in xrange(ty):
        for x in xrange(tx):
            points.sort(lambda a, b: dist((x, y), a) - dist((x, y), b))
            res[y][x] = points[0] if dist((x, y), points[0]) != dist((x, y), points[1]) else '.'
    return res 

def countFill(fill, p):
    c = 0
    for y in xrange(len(fill)):
        c+= fill[y].count(p)
    return c

fill = fillArea((400, 400), inpt)

def getPotential(fill):
    notRel = set()
    for y in xrange(len(fill)):
        for x in xrange(len(fill[0])):
            if x == 0 or y == 0 or x == len(fill[0]) -1 or y == len(fill) -1: notRel.add(fill[y][x])
    return [x for x in inpt if x not in notRel]

        
potential = getPotential(fill)


print(max([countFill(fill, p) for p in potential]))


    