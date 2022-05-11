print('Ласкаво просимо до ЧуДоВоГо калькулятору (версія 0.3) ')
print('Тепер я також вмію швидко складати багато чисел. Спробуй нову операцію "+++"')
print('Оберіть операцію (+, -, *, /, +++):')
b = input('Выберите операцию: ')
if b == '*':
    a = int(input('Введите первое целое число: '))
    c = int(input('Введите второе целое число :'))
    print(a, '*', c, '=', a*c)
elif b == '/':
    a = int(input('Введите первое целое число: '))
    c = int(input('Введите второе целое число :'))
    print(a, '/', c, '=', a/c)
elif b == '+':
    a = int(input('Введите первое целое число: '))
    c = int(input('Введите второе целое число :'))
    print(a, '+', c, '=', a+c)
elif b == '-':
    a = int(input('Введите первое целое число: '))
    c = int(input('Введите второе целое число :'))
    print(a, '-', c, '=', a-c)
elif b == '+++':
    text = []
    new_element = None
    while new_element != '':
        new_element = (input('Введіть число та натисніть Enter (якщо бажаете завершити, просто натисніть Enter):'))
        try:
            text.append(int(new_element))
        except ValueError:
            new_element = ''

    text2 = text.copy()
    print(sum(text2))
else:
    print("Неверная операция")