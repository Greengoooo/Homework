alf =  'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
message = input("Сообщение для шифровки(только a-z, A-Z:) ")
smeshenie = int(input('Шаг шифровки: '))
deistvie = input("Введите 1 для шифрования, 2 для дешифрования:")
itog = ''
if deistvie == '1':
    for i in message:
        place = alf.find(i)
        new_place = place + smeshenie
        if i in alf:
            itog += alf[new_place]
        else:
            itog += i
elif deistvie == '2':
    for i in message:
        place = alf.find(i)
        new_place = place - smeshenie
        if i in alf:
            itog += alf[new_place]
        else:
            itog += i
else:
    print('Не верное действие')
print(itog)
