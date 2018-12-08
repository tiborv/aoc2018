import sys


data = [int(n) for n in sys.stdin.readline().strip().split(" ")]

def parse(data):
    numOfchildren, numOfMeta = data[:2]
    currentData = data[2:]
    total = [] 

    for i in xrange(numOfchildren):
        value, currentData = parse(currentData)
        total += [value]

    currentMeta = currentData[:numOfMeta]
    restData = currentData[numOfMeta:]

    if numOfchildren == 0:
        return sum(currentMeta), restData

    total = [total[i-1] for i in currentMeta  if i-1 < len(total)]
    return sum(total), restData

total, remaining = parse(data)

print(total)
        

