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

def cartSort(a, b):
    if a['y'] == b['y']:
        return a['x'] - b['x']
    return a['y'] - b['y']

crossTurnRight = lambda (dir): (dir + 1) % 4
crossTurnLeft = lambda (dir): (dir + 3) % 4
def upTurn(dir):
    if dir == 0:
        return 3
    if dir == 1:
        return 2
    if dir == 2:
        return 1
    return 0

def downTurn(dir):
    if dir == 0:
        return 1
    if dir == 1:
        return 0
    if dir == 2:
        return 3
    return 2


while True:
    carts.sort(cartSort)
    cont = True
    for cart in carts:
        nextY = cart['y'] + dirY[cart['d']]
        nextX = cart['x'] + dirX[cart['d']]
        if track[nextY][nextX] == '\\':
            cart['d'] = upTurn(cart['d'])
        if track[nextY][nextX] == '/':
            cart['d'] = downTurn(cart['d'])
        if track[nextY][nextX] == '+':
            if cart['i'] == 0:
                cart['d'] = crossTurnLeft(cart['d'])
            if cart['i'] == 2:
                cart['d'] = crossTurnRight(cart['d'])
            cart['i'] = (cart['i'] + 1) % 3

        if (nextY,nextX) in [(other['y'], other['x']) for other in carts]:
            carts = filter(lambda otherCart: (otherCart['x'], otherCart['y']) not in [(cart['x'], cart['y']), (nextX, nextY)] , carts)
        
        cart['y'] = nextY
        cart['x'] = nextX
    if len(carts) == 1:
        break
print(carts[0]['x'], carts[0]['y'])
