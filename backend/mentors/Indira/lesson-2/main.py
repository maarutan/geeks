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

day = int(input(f" Введите день рождения (только число): "))
mouth = int(input(f" Введите месяц рождения (только число): "))

if day < 1 or day > 31 or mouth < 1 or mouth > 12:
    print("\nВы ошиблись в вводе!!!\nправильный ввод: <day,month>: <(1-31) (1-12)>")
else:
    if mouth == mar and day >= 21 or mouth == apr and day <= 20:
        sing = "овен"
    elif mouth == apr and day >= 21 or mouth == mai and day <= 21:
        sing = "Телец"
    elif mouth == mai and day >= 22 or mouth == jun and day <= 21:
        sing = "Близнецы"
    elif mouth == jun and day >= 22 or mouth == jul and day <= 22:
        sing = "Рак"
    elif mouth == jul and day >= 23 or mouth == aug and day <= 21:
        sing = "Лев"
    elif mouth == aug and day >= 22 or mouth == sep and day <= 23:
        sing = "Дева"
    elif mouth == sep and day >= 24 or mouth == octo and day <= 23:
        sing = "Весы"
    elif mouth == octo and day >= 24 or mouth == nov and day <= 22:
        sing = "Скорпион"
    elif mouth == nov and day >= 23 or mouth == dec and day <= 22:
        sing = "Стрелец"
    elif mouth == dec and day >= 23 or mouth == jan and day <= 20:
        sing = "Козерог"
    elif mouth == jun and day >= 21 or mouth == feb and day <= 19:
        sing = "Водолей"
    elif mouth == feb and day >= 22 or mouth == mar and day <= 20:
        sing = "Рыбы"


print(f"\nваш день: {day}")
print(f"ваш месяц: {mouth}")
print("-----------------")
print(f"вы: {sing}")
