print('Добро пожаловать в сравнитель чисел!')
A = int(input('Введите первое число: '))
B = int(input('Введите второе число: '))
if A > B:
    print(A, '>', B)
elif A == B:
    print(A, '=', B)
elif A < B:
    print(A, '<', B)
else:
    print('Impossible')