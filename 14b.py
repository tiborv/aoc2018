

r = "3710"
l1, l2 = 0, 1

inpt = "047801"
while True:
    r += str(int(r[l1]) + int(r[l2]))
    l1 = (l1 + int(r[l1]) + 1) % len(r)
    l2 = (l2 + int(r[l2]) + 1) % len(r)

    if inpt in r[-8:]:
        break

print(r.find(inpt))



