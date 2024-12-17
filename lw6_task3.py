n1 = input('Введите число - n, которое является количеством элементов в одномерном списке - ')
while True:
    try:
        if n1[0] == '-':
            raise Exception
        int(n1)
    except Exception:
        n1 = input('Число некорректно. Введите число - n, которое является количеством элементов в одномерном списке - ')
    else:
        n1 = int(n1)
        break
n = []
f = 0
max = -999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
for i in range(n1):
    a = input('Введите число: ')
    while True:
         try:
            if a[-1] != ',':
                 for i in range(len(a)):
                    if a[i] == ',':
                        a = a[:i] + '.' + a[i+1:]
            if ('-00' not in a[:3]) and ('00' not in a[:2]) and (a[0] in '-0987654321'):
                float(a)
            else:
                raise Exception
         except Exception:
             a = input('Введенные значения не являются числом, введите число: ')
         else:
            if a[0] == '-' and float(a[1:]) > max:
                max = float(a[1:])
                f = len(n)
            elif float(a) > max:
                max = float(a)
                f = len(n)
            n = n + list([float(a)])
            break
summ_2 = 0
count_2 = 0
comp = 0
for i in range(len(n)):
    if n[i]%2 == 0:
        summ_2 += n[i]
        count_2 += 1
    if i == f and i != len(n)-1:
        comp = 1
        for j in range(i+1,len(n)):
            comp *= n[j]
print ('Сумма элементов кратных двух равна = ', summ_2)
print ('Количество элементов кратных двух равно = ', count_2)
print ('Произведение чисел, стоящих после максимального равно = ', comp)