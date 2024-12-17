text = input('Введите текст:')
count1 = 0
count2 = 0
f = 0
for i in text:
    if i == '(':
        count1 += 1
    elif i == ')':
        count2 += 1
    if count2 > count1:
        print('В данном тексте скобки не сбалансированны')
        f = 1
        break
if count1 == count2:
    print('В данном тексте скобки сбалансированны')
elif f == 0:
    print('В данном тексте скобки не сбалансированны')