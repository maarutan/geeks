mentors = ["Тимур", "Арсен", "Гулина", "Даниель"]

while True:
    print("\nКоманды:")
    print("1. Добавить")
    print("2. Изменить")
    print("3. Удалить")
    print("0. Выход")
    print("-----------------")

    command = input("Введите команду: ")

    if command == "1":
        name = input("Введите имя ментора: ").title()

        if len(name) > 15:
            print("-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!")
            print("Имя должно содержать не более 15 букв !!!")
            print("-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!")
            continue

        if name in mentors:
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("Это имя уже присутствует !!!")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            continue

        if len(mentors) >= 10:
            print("Список менторов переполнен")
            continue

        mentors.append(name)
        print("!-!-!-!-!-!")
        print("Успешно добавлено!")
        print("!-!-!-!-!-!")
        print(mentors)
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    elif command == "2":
        old_name = input("Введите старое имя: ").title()

        if old_name not in mentors:
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("Имя не найдено в списке !!!")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            continue

        new_name = input("Введите новое имя ментора: ").title()

        if len(new_name) > 15:
            print("-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!")
            print("Имя должно содержать не более 15 букв !!!")
            print("-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!")
            continue

        if new_name in mentors:
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("Это имя уже присутствует !!!")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            continue

        index = mentors.index(old_name)
        mentors[index] = new_name
        print("!-!-!-!-!-!")
        print("Успешно изменено!")
        print("!-!-!-!-!-!")
        print(mentors)
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    elif command == "3":
        delete_option = input(
            "\nУдаление по ???\n1) Имени\n2) Индексу\n----(1) / (2)----\nВвод: "
        )

        if delete_option == "1":
            name_to_remove = input("Введите имя для удаления: ").title()

            if name_to_remove in mentors:
                mentors.remove(name_to_remove)
                print("Имя успешно удалено!")
                print(mentors)
            else:
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print("Имя не найдено в списке !!!")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

        elif delete_option == "2":
            try:
                index = int(input("Введите индекс для удаления: "))
                if 0 <= index < len(mentors):
                    del mentors[index]
                    print("Элемент успешно удалён!")
                    print(mentors)
                else:
                    print("Некорректный индекс.")
            except ValueError:
                print("Введите корректный индекс.")

    elif command == "0":
        mentors_tuple = tuple(mentors)
        print("Список менторов в кортеже:")
        print(mentors_tuple)
        break

    else:
        print("Некорректная команда.")
