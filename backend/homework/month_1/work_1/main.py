mon = float(
    input(
        """Cколько вы потратели ???
[за Понидельник]: """
    )
)
tue = float(
    input(
        """Cколько вы потратели ???
[за Вторник]: """
    )
)
wed = float(
    input(
        """Cколько вы потратели ???
[за Среду]: """
    )
)
thu = float(
    input(
        """Cколько вы потратели ???
[за Чертверк]: """
    )
)
fri = float(
    input(
        """Cколько вы потратели ???
[за Пятницу]: """
    )
)
sat = float(
    input(
        """Cколько вы потратели ???
[за Субботу]: """
    )
)

sun = float(
    input(
        """Cколько вы потратели ???
[за Воскрисения] """
    )
)

totalSum = mon + tue + wed + thu + fri + sat + sun
totalSum = round(totalSum, 1)

average = totalSum / 7
average = round(average, 1)

print(f"общая сумма потраченных денег за неделю : {totalSum} cомов")
print(f"также средняя сумма потраченных денег {average} сомов")


if totalSum >= 1 and totalSum <= 100:

    print("потрачено мало")
elif totalSum > 101 and totalSum <= 500:
    print("потрачено нормально")
elif totalSum > 501:
    print("потрачено много")
else:
    print("не было трат")


print("hello world")


# weeks = [
#     "Понедельник",
#     "Вторник",
#     "Среда",
#     "Четверг",
#     "Пятница",
#     "Суббота",
#     "Воскресенье",
# ]

# results = []
# try:
#     for days in weeks:
#         result = float(input(f"сколько вы потратили за {days}???: "))
#         results.append(result)

#     totalSum = round(sum(results), 1)
#     average = round(totalSum / 7)

#     print(f"общая сумма потраченных денег за неделю : {totalSum} cомов")
#     print(f"также средняя сумма потраченных денег {average} сомов")

#     if totalSum >= 1 and totalSum <= 100:
#         print("потрачено мало")
#     elif totalSum > 101 and totalSum <= 500:
#         print("потрачено нормально")
#     elif totalSum > 501:
#         print("потрачено много")
#     else:
#         print("не было трат")


# except ValueError:
#     print("вы ввили строку ввидите число")


# while True:
#     color = input(
#         "Введите цвет светофора \n(зеленый, желтый, красный) или 'выход/exit'\n для завершения: "
#     ).lower()

#     if color == "зеленый" or color == "green":
#         print("")
#         print("Иди!")
#         print("")
#     elif color == "желтый" or color == "yellow":
#         print("")
#         print("Жди!")
#         print("")
#     elif color == "красный" or color == "red":
#         print("")
#         print("Стой!")
#         print("")
#     elif color in "выход exit":
#         print("")
#         print("Выход из программы.")
#         break
#     else:
#         print("Неверный запрос! Попробуйте ещё раз.")
