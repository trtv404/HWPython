# Задача 18: Требуется найти в массиве A[1..N] самый близкий 
# по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random

length = int(input('Ведите количество элементов в массиве: '))
my_list = [random.randint(0, 100) for _ in range(length)]
print(my_list)

numb = int(input("Какое число искать: "))
close_num = my_list[0]

for i in my_list:
    diff = abs(numb - close_num)
    if abs(i - numb) <= diff:
        close_num = i

print(f'Самое близкое к числу {numb} является число {close_num}')
