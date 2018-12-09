nOfPlayers = 428
lastMarbleScore = 70825

marbles = [0, 2, 1, 3]
curr = 1
elf = 3
score = {}
for i in xrange(1, nOfPlayers + 1):
    score[i] = 0

def printCurr(c, marbles):
    print "[",
    for p in xrange(len(marbles)):
        print marbles[p] if c != p else "(" + str(marbles[p]) + ")",
    print "]"


for marble in xrange(4, lastMarbleScore + 1):
    elf = (elf % nOfPlayers) + 1
    if marble % 23 == 0:
        curr -= 9
        score[elf] += marble + marbles[curr]
        del marbles[curr]
        curr = (curr + 2) % (len(marbles) + 1)
        continue
    if curr % (len(marbles) + 1) == 0:
        curr = 1
    marbles.insert(curr, marble)
    curr = (curr + 2) % (len(marbles) + 1)
print(max(score.values()))