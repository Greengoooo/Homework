text = input("Введите текст: ") 
text = text.replace(str('>:('), '😠')
text = text.replace(str('>:)'), '😈')
text = text.replace(str(':)'), '🙂')
text = text.replace(str('XD'), '😂')
text = text.replace(str(':('), '🙁')
print(text)