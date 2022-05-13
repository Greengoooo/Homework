import time
import random

print('Зараз буде змійка :3')
a = '*'
b = 5
while True:
    try:
        time.sleep(0.1)
        b += (random.randint(-1, 1))
        a = '*'
        n = ' '
        fix = n * b + a
        print(fix)
    except KeyboardInterrupt:
        break
c = '0_0'
print(n * b + c)
