import sys

lines = [list(line.strip()) for line in sys.stdin]    


def find(lines):
    nlines = len(lines)
    for x in xrange(nlines):
        for y in xrange(nlines):
            if x == y:
                continue
            alist, blist = list(lines[x]), list(lines[y])
            l = len(alist)
            diff = [alist[i] == blist[i] for i in xrange(l)]

            if diff.count(False) != 1:
                continue
            common = [alist[i] if diff[i] else "" for i in xrange(l)]
            return "".join(common)


print(find(lines))