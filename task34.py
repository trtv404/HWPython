# Урок 7. Функции высшего порядка
# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, 
# если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с 
# ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  

poem = input('введите стих: ')
print(poem)
vowel = ['а', 'я', 'и', 'ы', 'о', 'ё', 'э', 'е', 'у', 'ю']
poem_list = list(poem.split())
print(poem_list)
res = list()
for i in poem_list:
    k=0
    for j in i: 
        if j in vowel: 
            k +=1
    res.append(k)
print(res)

if len(set(res)) == 1: 
    print('Парам пам-пам')
else:
    print('Пам парам')