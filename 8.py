import sys


data = [int(n) for n in sys.stdin.readline().strip().split(" ")]

def parse(data):
    numOfchildren, numOfMeta = data[:2]
    currentData = data[2:]
    totalMetasum = 0

    for i in xrange(numOfchildren):
        metasum, currentData = parse(currentData)
        totalMetasum += metasum

    currentMeta = currentData[:numOfMeta] 
    restData = currentData[numOfMeta:] 

    return totalMetasum + sum(currentMeta), restData

total, remaining = parse(data)

print(total)
        

