text = input('Введите строку:')
textend = ''

for i in text:
    if i != ' ' and i not in textend:
        textend = textend + i
print('Получившаяся строка имеет вид -', textend)
