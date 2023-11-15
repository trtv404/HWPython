# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены 
# только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте
# выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля 
# и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

import random

a = int(input('Количество кустов: '))

list = [random.randint(0,10) for _ in range(a)]
print(list)
i = 1
first=list[0]+list[1]+list[-1]
print(f'первый {first}')
last=list[0]+list[-1]+list[-2]
print(f'последний {last}')
max = first
position = 0
if first < last: 
    max = last
    position = len(list)
while i < len(list)-1:
    print(list[i] + list[i-1] + list[i+1])
    if list[i] + list[i-1] + list[i+1] > max: 
        max = list[i] + list[i-1] + list[i+1]
        position = i
    i+=1
print(f'с куста по индексу {position} и соседних можно собрать {max} ягод')