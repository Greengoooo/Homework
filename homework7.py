
SIZE = 5

for x in range(SIZE):
    for y in range(SIZE):
        for z in range(SIZE):
            if sum((
                x == 0 or x == SIZE -1,
                y == 0 or y == SIZE -1,
                z == 0 or z == SIZE -1,
            )) >=2:
                place(x, z, y)



SIZE = 4 

for x in range(SIZE):
    for y in range(SIZE):
        if x == 0 or y == 0 or x == SIZE - 1 or y == SIZE - 1:
            place(x,0,y)



RADIUS = 10
rad2 = RADIUS ** 2

for x in range(-RADIUS, RADIUS + 1):
    for y in range(-RADIUS, RADIUS + 1):
        if rad2 * 1.1 >= x ** 2 + y ** 2 >= rad2 * 0.9:
            place (x,y,0)

