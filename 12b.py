import sys

initState = list(sys.stdin.readline().split(':')[1].strip())

rules = {}
for r in sys.stdin.readlines()[1:]:
    key, res = [rr.strip() for rr in r.split('=>')]
    rules[key] = res


def update(state, zeroIdx):
    state = ['.', '.', '.', '.'] + state + ['.', '.', '.', '.']
    result = []
    for i in xrange(2, len(state) - 2):
        section = "".join(state[i-2: i + 3])
        result.append(rules[section] if section in rules else '.')
    return result, zeroIdx + 2

def count(state, idxPos):
    sum = 0
    for i in range(-idxPos, len(state) - idxPos):
        sum  += i if state[idxPos + i] == "#" else 0
    return sum

state = initState
idxPos = 0
prevScore = 0

convergenceIterations = 2000
for i in xrange(convergenceIterations):
    state, idxPos = update(state, idxPos)
    score = count(state, idxPos)
    diff = score - prevScore 
    prevScore = score


print(score + ((50000000000 - convergenceIterations) * diff))

