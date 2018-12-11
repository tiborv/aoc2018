 
gridSerial = 5235

def powerlvl(x, y):
    plvl = (((x + 10) * y) + gridSerial) * (x + 10)
    return  int(str(plvl)[-3])-5 if plvl > 99 else -5

powerLevels = {}
for y in xrange(1, 301):
    for x in xrange(1, 301):
        powerLevels[(x, y)] = powerlvl(x, y)

def checkGrid(x, y, s):
    return sum([powerLevels[(x+xi, y+yi)] for yi in xrange(s) for xi in xrange(s)])


maxPower = 0
cord = (0,0)
for y in xrange(1, 301):
    for x in xrange(1, 301):
        for s in xrange(1, 301 - max(x,y)):
            power = checkGrid(x, y, s)
            if power > maxPower:
                maxPower = power
                cord = [(x, y), s]

print(maxPower, cord)

