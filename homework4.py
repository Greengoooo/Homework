print('Добро пожаловать в НеВеРоЯтНыЙ калькулятор (версия 0.2)')
b = input('Выберите операцию: ')
a = int(input('Введите первое целое число: '))
c = int(input('Введите второе целое число :'))
if b == '*':
    print(a, '*', c, '=', a*c)
elif b == '/':
    print(a, '/', c, '=', a/c)
elif b == '+':
    print(a, '+', c, '=', a+c)
elif b == '-':
    print(a, '-', c, '=', a-c)
else:
    print("Неверная операция")