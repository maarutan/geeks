rounds = 12

while rounds > 0:
    jan = 1
    feb = 2
    mar = 3
    apr = 4
    mai = 5
    jun = 6
    jul = 7
    aug = 8
    sep = 9
    octo = 10
    nov = 11
    dec = 12

    exits = ["exit", "выход", "stop", "стоп", "quit", "выйти"]

    day = input(f" Введите день рождения ({rounds}): ")
    if day.lower() in exits:
        break

    month = input(f" Введите месяц рождения ({rounds}): ")
    if month.lower() in exits:
        break

    year = input(f" Введите год рождения ({rounds}): ")
    if year.lower() in exits:
        break

    if not (day.isdigit() and month.isdigit() and year.isdigit()):
        print("")
        print("!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!")
        print("Вы ошиблись. Введите только числа или 'exit/выход'")
        print("!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!")
        print("")
        rounds -= 1
        continue

    day = int(day)
    month = int(month)
    year = int(year)
        

    try:
        if (day > 31 or day < 1 and month < 1 or month > 12 or year <= 1900 or year > 2024):
            print(" ")
            print("Вы ошиблись в вводе!!!\nправильный ввод: <day,month,year>: <(1-31) (1-12) (1900-2024)>")
            sing = "из-за ошибки у вас неопределен знак задиака"
            print(" ")
        else:
            if (month == mar and day >= 21) or (month == apr and day <= 20):
                sing = "овен"
            elif (month == apr and day >= 21) or (month == mai and day <= 21):
                sing = "телец"
            elif (month == mai and day >= 22) or (month == jun and day <= 21):
                sing = "близницы"
            elif (month == jun and day >= 22) or (month == jul and day <= 22):
                sing = "рак"
            elif (month == jul and day >= 23) or (month == aug and day <= 21):
                sing = "лев"
            elif (month == aug and day >= 22) or (month == sep and day <= 23):
                sing = "дева"
            elif (month == sep and day >= 24) or (month == octo and day <= 23):
                sing = "весы"
            elif (month == octo and day >= 24) or (month == nov and day <= 22):
                sing = "скорпион"
            elif (month == nov and day >= 23) or (month == dec and day <= 22):
                sing = "стрелец"
            elif (month == dec and day >= 23) or (month == jan and day <= 20):
                sing = "козерог"
            elif (month == jan and day >= 21) or (month == feb and day <= 19):
                sing = "водолей"
            elif (month == feb and day >= 20) or (month == mar and day <= 20):
                sing = "рыбы"
            else:
                print(" ")
                sing = "неопределенный знак зодиака"
                print("Кажется у вас ошибка попробуйте заного")
                print(" ")

            print(" ")
            print(f' День: {day}, \n Месяц: {month}, \n Год: {
                year}, \n Знак задиака: {sing.title()}.')
            print("___________________________")
            print(f" {day}.{month}.{year}")
            print("")
    except ValueError:
        print('вы не правильно ввили повторите попытку только числа')
    rounds -= 1
