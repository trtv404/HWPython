# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. 
# n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
#ввод цифр вручную заменила на рандом
import random

arr_len_1 = int(input("Введите кол-во элементов первого множества "))
arr_len_2 = int(input("Введите кол-во элементов второго множества "))

array1 = [random.randint(0, 10) for _ in range(arr_len_1)]
array2 = [random.randint(0, 10) for _ in range(arr_len_1)]
print(array1) #вывести чтобы наглядно проверить
print(array2) #вывести чтобы наглядно проверить

commom = set(array1).intersection(set(array2)) #для уникальности превращаю во множество

list1 = list(commom) #так как множествомодет быть  не упорядочено, а надо упорядочить. Возвращаю в list
# сортировка пузырьком
i = 0
j = 0
while i < len(list1)-1:
    while j < len(list1)-1:
        if list1[i] > list1[i+1]:
            temp = list1[i]
            list1[i] = list1[i+1]
            list1[i+1] = temp
        i+=1
        j+=1

print(list1)




