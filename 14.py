

r = "3710"
l1, l2 = 0, 1

inpt = 47801
while True:
    s = int(r[l1]) + int(r[l2])
    r = r + str(s)
    l1 = (l1 + int(r[l1]) + 1) % len(r)
    l2 = (l2 + int(r[l2]) + 1) % len(r)

    if len(r) > 10 + inpt:
        break

print(r[inpt: inpt + 10])



