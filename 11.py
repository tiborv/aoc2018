 
gridSerial = 5235
def powerlvl(x, y):
    rid = x + 10
    plvl = (rid * y) + gridSerial
    plvl *= rid
    plvl = int(str(plvl)[-3]) if plvl > 99 else 0
    return plvl - 5

def checkGrid(x, y):
    x1, y1, x2, y2 = x + 1, y + 1, x + 2, y + 2
    return sum([
        powerlvl(x, y),
        powerlvl(x1, y),
        powerlvl(x2, y),
        powerlvl(x, y1),
        powerlvl(x1, y1),
        powerlvl(x2, y1),
        powerlvl(x, y2),
        powerlvl(x1, y2),
        powerlvl(x2, y2),
    ])
maxPower = 0
cord = (0,0)
for y in xrange(1, 301):
    for x in xrange(1, 301):
        power = checkGrid(x, y)
        if power > maxPower:
            maxPower = power
            cord = (x, y)
print(maxPower, cord)

