main_menu = '''Главное меню:
    1. Открыть файл
    2. Сохранить файл
    3. Показать все контакты
    4. Создать контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход'''

choice_menu = '\n Выберете пункт меню: '

empty_list_or_not_open_file = 'Телефонная книга пуста или файл не открыт!'

successful_open = 'файл открыт успешно'
succcessful_save = 'файл сохранен успешно '

def successful_edited(name: str) -> str:
    return f'Контакт {name} успешно изменен'

new_name = 'Введите новые ФИО: '
new_phone = 'Введите новый телефон: '
new_comment = 'Введите новый комментарий: '

def contact_saved(name: str) -> str:
    return f'Контакт {name} успешно сохранен'

def not_found(word: str) -> str:
    return f'Контакты содержащие {word} не найдены'

new_contact = 'Контакт успешно добавлен'

input_keyword = 'Введите искомый элемент'

input_index = 'Введите индекс(порядковый номер) контакта: '

enter_or_empty = 'Введите новые значения или оставьте пустым для сохранениия оригиинального значения'

input_delete_index = 'Введите индекс контакта, который хотите удалить: '

def delete_contact(name: str) -> str:
    return f'Контакт {name} удален'

def confirm_delete(name: str) -> str:
    return f'Вы точно хотите удалить контакт {name}?'

bye_bye = 'До свидания'

no_saved_book = 'Есть несохраненные изменения. Сохратить?'
# succcessful_edited = 'Контак успешно изменен'
