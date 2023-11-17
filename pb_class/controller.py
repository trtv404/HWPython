import view
import text_fields as txt
from classes import Contact, PhoneBook

def start():
    phonebook = PhoneBook('pb_class\sample.txt')
    while True:
        choice = view.main_menu()
        match choice:
            case 1:                         # 1. Открыть файл
                phonebook.open()
                view.print_info(txt.successful_open)
            case 2:                         # 2. Сохранить файл
                phonebook.save()
                view.print_info(txt.succcessful_save)
            case 3:                         # 3. Показать все контакты
                pb = phonebook.get()
                view.show_contacts(pb, txt.empty_list_or_not_open_file)
                pass
            case 4:                         # 4. Создать контакт
                new_contact = view.new_contact()
                phonebook.add(new_contact)
                view.print_info(txt.contact_saved(new_contact.name))
            case 5:                        # 5. Найти контакт
                word = view.enter_keyword()
                result = phonebook.find(word)
                view.show_contacts(result, txt.not_found(word))
            case 6:                         # 6. Изменить контакт
                pb = phonebook.get()
                view.show_contacts(pb, txt.empty_list_or_not_open_file)
                if pb:
                    edited_contact = view.edit_contact(pb, txt.input_index)
                    phonebook.edit_contact(edited_contact)
                    view.print_info(txt.succcessful_edited(edited_contact[1].name))

            case 7:                         # 7. Удалить контакт
                pb = phonebook.get()
                view.show_contacts(pb, txt.empty_list_or_not_open_file)
                if pb:
                    index = view.input_index(pb, txt.input_delete_index)
                    if view.confirtm(txt.confirm_delete(pb[index-1].name)):
                        view.print_info(txt.delete_contact(phonebook.remove(index)))
            case 8:                         # 8. Выход
                if phonebook.save_on_exit():
                    if view.confirtm(txt.no_saved_book):
                        phonebook.save()
                view.print_info(txt.bye_bye)
                exit()
            
