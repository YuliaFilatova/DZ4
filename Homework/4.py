#Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.(записать в строку)
#Пример:
#k=2 => 2*x^2 + 4*x + 5 или x^2 + 5 или 10*x**2
#k=3 => 2*x^3 + 4*x^2 + 4*x + 5

import itertools
from random import randint

k = int(input("Введите степень k: "))

factor = []
for i in range(1, k +2):
    factor.append(randint(1, 101))

result = []
for i in range(len(factor)):
    if k == 1:
        result.append(f'{factor[i]}*x')
    elif k == 0:
        result.append(f'{factor[i]}')
    else:
        result.append(f'{factor[i]}*x^{k}')
    signs = randint(0, 1)
    if signs == 1:
        result.append('+')
    elif signs == 0:
        result.append('-')
    k -= 1

result.pop(-1)
result.append('=0')

record = open('file.txt', 'w')
record.write(''.join(result))
record.close()