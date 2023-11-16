# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

# для создания tel_book.txt 
# file = open('tel_book.txt', 'a', encoding='UTF-8')
# file.writelines('''Иванов Иван; 1111111; первый конт
# Петров Петр; +2(222)2222222; второй конт
# Семенов Семен; +3(333)3333333; третий конт
# Петрова Полина; +2(222)2222222; четвертый конт
# Федоров Федор; +5555; пятый
# кузнецов; 666; проверкр
# Сидоров Сидор; +1(333)1111111; восьмой конт''')
# file.close


# #меню
# menu = int(input('''Для просмотра тел.справочника введите 1.  
#     Для добавления контакта введите 2.
#     Для поиска контакта введите 3.
#     Для удаления контакта введите 4.
#     Для редактирования контакта введите 5.
#     ввод:'''))
# #просмотр
# if menu == 1:
#     file = open('tel_book.txt', 'r', encoding='UTF-8')
#     data = file.read()
#     print(data)
#     file.close

# #добавлениие
# elif menu == 2:
#     file = open('tel_book.txt', 'a', encoding='UTF-8')
#     file.writelines(input('ФИО: ') + '; ' + input('номер: ') + '; ' + input('примечание: ') + '\n')
#     print('Контакт добавлен!!!')
#     file.close

# #поиск контакта
# elif menu == 3:
#     file = open('tel_book.txt', 'r', encoding='UTF-8')
#     data = file.read()
#     cont_list = data.splitlines()
#     find = input('Введите ФИО, номер или комментарий, и будут показаны все пользователи, у которых есть указанная информация:')
#     for i in cont_list:
#         if find.lower() in i.lower(): 
#             print(i)

# #удаление
# elif menu == 4:
#     file = open('tel_book.txt', 'r', encoding='UTF-8')
#     data = file.read()
#     cont_list = data.splitlines()
#     find = input('Введите ФИО, номер или комментарий, и будут удалены все пользователи, у которых есть указанная информация:')
#     index = 0
#     while index < len(cont_list):
#         if find.lower() in cont_list[index].lower(): 
#             print(f'контакт {cont_list[index]} удален')
#             del cont_list[index]
#         index +=1
#     file.close
#     file = open('tel_book.txt', 'w', encoding='UTF-8')
#     for i in cont_list:
#         file.writelines(f'{i}\n')
#     file.close

# #редактирование контакта
# elif menu == 5:
#     file = open('tel_book.txt', 'r', encoding='UTF-8')
#     data = file.read()
#     cont_list = data.splitlines()
#     find = input('Введите ФИО, номер или комментарий контакта, который хотите редактировать: ')
#     index = 0
#     while index < len(cont_list):
#         if find.lower() in cont_list[index].lower(): 
#             print(f'Найдено {cont_list[index]}')
#             contact = cont_list[index].split('; ')
#             for i in range(0, len(contact)):
#                 print(f'{contact[i]} нужно заменить на (введите новые данные): ')
#                 contact[i] = input()
#             cont_list[index] = '; '.join(contact)
#         index +=1
    
#     file.close
#     file = open('tel_book.txt', 'w', encoding='UTF-8')
#     for i in cont_list:
#         file.writelines(f'{i}\n')
#     print('данные изменены')
#     file.close

