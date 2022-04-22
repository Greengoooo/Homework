text = input('Введите предложение со словом cucumber :')
if 'cucumber' not in text:
    print('OOPS mistake((((')
else:
    print(text[text.find('cucumber'):])
