BASE = 18

print('Привет, я конвентирую в базу 10 з бази 18')
print('Возможные символы и их значение')

for i in range(BASE):
    if i < 10:
        print(f'{i}={i}')
    else:
        print(f'{chr(ord("A")- 10 + i)} = {i}')

print()
inp_num = input(f'Введите чисто в базе {BASE}: ')

dec_value = 0
for i, char in enumerate(reversed(inp_num)):
    if char.isdigit():
        digit = int(char)
    elif 9 < ord(char) - (ord('A') - 10) < BASE:
        digit = ord(char) - (ord('A') - 10)
    else:
        print(f'Введенное число не соответствует базе {BASE}')
        dec_value = None
        break

    dec_value += digit * BASE ** i

if dec_value is not None:
    print(f'{inp_num} = {dec_value}')
