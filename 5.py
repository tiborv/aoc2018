import sys

lst = list(sys.stdin.readline())


def exp(lst):
    res, i, exploded = [], 0, False
    while i < len(lst) - 1:
        if lst[i] != lst[i+1] and lst[i].upper() == lst[i+1].upper():
            i+=2
            exploded = True
            if not i < len(lst):
                return res, exploded
            continue
        res.append(lst[i])
        i+=1
    res.append(lst[-1])
    return res, exploded
        
exploded = True
while exploded:
    lst, exploded = exp(lst)

print(len(lst))

