# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума
# и не больше заданного максимума)

import random
length = int(input('Ведите длинну массива: '))
list = [random.randint(0, 100) for _ in range(length)]
print(list)

min = int(input('Ведите минимум: '))
max = int(input('Ведите максимум: '))

i = 0
while i < len(list):
    if list[i] >= min and list[i] <= max: print(f'индекс {i}') 
    i+=1

# for i in range(len(list)):
#     if min<= list[i] <= max:
#         print(i)