import sys
track = [list(line) for line in sys.stdin]     

dirY = [-1, 0, 1, 0]
dirX = [0, 1, 0, -1]

carts = []
for y in range(len(track)):
    for x in range(len(track[y])):
        if track[y][x] == '^':
            track[y][x] = '|'
            carts.append({
                'y': y,
                'x': x,
                'd': 0,
                'i': 0
            })
        if track[y][x] == '>':
            track[y][x] = '-'
            carts.append({
                'y': y,
                'x': x,
                'd': 1,
                'i': 0
            })
        elif track[y][x] == 'v':
            track[y][x] = '|'
            carts.append({
                'y': y,
                'x': x,
                'd': 2,
                'i': 0
            })
        elif track[y][x] == '<':
            track[y][x] = '-'
            carts.append({
                'y': y,
                'x': x,
                'd': 3,
                'i': 0
            })

turnRight = lambda (currentDir): (currentDir + 1) % 4
turnLeft = lambda (currentDir): (currentDir + 3) % 4

while True:
    cont = True
    carts = sorted(carts, key=lambda cart:(cart['y'], cart['x']))
    for cart in carts:
        nextY = cart['y'] + dirY[cart['d']]
        nextX = cart['x'] + dirX[cart['d']]
        if track[nextY][nextX] == '\\':
            cart['d'] = {0: 3, 1:2, 2:1, 3:0}[cart['d']]
        elif track[nextY][nextX] == '/':
            cart['d'] = {0: 1, 1:0, 2:3, 3:2}[cart['d']]
        elif track[nextY][nextX] == '+':
            if cart['i'] == 0:
                cart['d'] = turnLeft(cart['d'])
            elif cart['i'] == 2:
                cart['d'] = turnRight(cart['d'])
            cart['i'] = (cart['i'] + 1)%3
        if (nextY,nextX) in [(other['y'], other['x']) for other in carts]:
            carts = [other for other in carts if (other['y'], other['x']) not in [(cart['y'], cart['x']),(nextY,nextX)]]
            cont = False
            print(nextX, nextY)
        cart['y'] = nextY
        cart['x'] = nextX
    if not cont:
        break
