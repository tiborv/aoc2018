import sys


inpt = []

for l in sys.stdin.readlines():
    pos = [int(p.strip()) for p in l.split("position=<")[1].split(">")[0].split(',')]
    vel = [int(p.strip()) for p in l.split("velocity=<")[1].split(">")[0].split(',')]
    inpt.append((pos, vel))
    

def printer(poslist):
    maxX, maxY, minX, minY = -9999999,-9999999,9999999,9999999
    s = set()
    for pos, vel in poslist:
        maxX, maxY, minX, minY = max(maxX,pos[0]), max(maxY,pos[1]), min(minX,pos[0]), min(minY,pos[1])
        s.add((pos[0], pos[1]))

    print("")
    for y in xrange(minY, maxY+1):
        for x in xrange(minX, maxX+1):
            print("#" if (x, y) in s else "."),
        print("")

def getlen(poslist):
    return max([pos[0] for pos, val in poslist]) - min([pos[0] for pos, val in poslist])
                
def update(poslist):
    return [[[pos[0]+vel[0], pos[1]+vel[1]], [vel[0], vel[1]]] for pos, vel in poslist]

minX = 99999999
prevInpt = []
i = 0
while True:
    inpt = update(inpt)
    currMin = getlen(inpt)
    if currMin > minX:
        printer(prevInpt)
        break
    minX = currMin
    prevInpt = inpt