from time import sleep
import os


countryFlags = {
    "kyrgyzstan": {"yellow", "red"},
    "russian": {"blue", "red", "white"},
}


def printCountry():
    print("")
    for cf in countryFlags:
        print(f'{cf} - {", ".join(countryFlags[cf])}')
    print("")
    sleep(2)


while True:
    print("\nВыберите команду\n1) Найти Страну\n2) Добавить Страну\n0) выход")
    print("~~~~(1/2/0)~~~~")
    print("______________________")

    userInput = input("Ввидите Команду: ")
    try:
        if userInput == "1":
            nameCountry = input("Ввидите имя старны: ")
            for country in countryFlags:
                if nameCountry in country:
                    os.system('clear')
                    print("__________________________________________")
                    print(f"Цвет стараны {nameCountry}",
                          ", ".join(countryFlags[nameCountry]))
                    print("------------------------------------------")
                    sleep(3)
                else:
                    os.system('clear')
                    print("----------------------------- !!!")
                    print("Не правильно ввили имя страны !!!")
                    print("----------------------------- !!!")
                    sleep(2)
        elif userInput == "2":
            nameCountry = input("Ввидите имя старны: ").lower()
            colorCountry = input("Введите цвет страны: ")
            colors = {color.strip() for color in colorCountry.split(",")}
            countryFlags[nameCountry] = colors
            printCountry()
        elif userInput == "0":
            for key, country in countryFlags:
                print(f'{country} - {countryFlags}')
                sleep(2)

            print()
            break
        else:
            os.system('clear')
            print("\n!-!-!-!-!-!-!-!-!-!-!-!-!-!-!")
            print("не корекнный ввод команды !!!")
            print("!-!-!-!-!-!-!-!-!-!-!-!-!-!-!")
            sleep(2)

    except ValueError:
        os.system('clear')
        print("не корекнный ввод команды!!!")
        sleep(2)
        continue
