# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.

num_lim = int(input("Введите число, до которого считать: "))
counter = 2
while counter <= num_lim:
    print(counter)
    counter = counter*2
