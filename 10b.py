import sys


inpt = []

for l in sys.stdin.readlines():
    pos = [int(p.strip()) for p in l.split("position=<")[1].split(">")[0].split(',')]
    vel = [int(p.strip()) for p in l.split("velocity=<")[1].split(">")[0].split(',')]
    inpt.append((pos, vel))

def getlen(poslist):
    return max([pos[0] for pos, val in poslist]) - min([pos[0] for pos, val in poslist])
                
def update(poslist):
    return [[[pos[0]+vel[0], pos[1]+vel[1]], [vel[0], vel[1]]] for pos, vel in poslist]

minX = 99999999
i = 0
while True:
    inpt = update(inpt)
    currMin = getlen(inpt)
    if currMin > minX:
        print(i)        
        break
    minX = currMin
    i+=1