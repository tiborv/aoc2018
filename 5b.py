import string
import sys

inpt = sys.stdin.readline()

def exp(lst):
    res, i, l, exploded = [], 0, len(lst), False
    while i < l - 1:
        if lst[i] != lst[i+1] and lst[i].upper() == lst[i+1].upper():
            i+=2
            exploded = True
            if not i < l:
                return res, exploded
            continue
        res.append(lst[i])
        i+=1
    res.append(lst[-1])
    return res, exploded


def explodeAll(lst):        
    exploded = True
    while exploded:
        lst, exploded = exp(lst)
    return len(lst)
        

m = 999999
for letter in "abcdefghijklmnopqrstuvwxyz":
    x = inpt.replace(letter, "").replace(letter.upper(), "")
    m = min(m, explodeAll(x))
print(m)
