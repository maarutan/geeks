# # Логический тип данных Операторы: Условные, Сравнения, Логические
#
# print(type(True))
# print(type(False))
#
#
# # если, иначеЕсли, иначе
#
# time = "день"
# if time == "утро":
#     print("доброе утро")
# elif time == 'день':
#     print("добрый день")
# elif time == "вечер":
#     print("добрый вечер")
# else:
#     print("Здравуйте ! (время суток не известно)")
#
# #
# # логические операторы
# # and or not
# #
# print(2 > 3 or 2 < 3)
# print(2 > 3 and 2 < 3)
# print(not False)
# print(not True)
#
# # операторы сравнения
# print(2 == 3)
# print(2 != 3)
# print(2 < 3)
# print(2 > 3)
# print(2 >= 3)
# print(2 <= 3)
# print(2 == 3)
# print(2 < 3)
# print(2 <= 3)
#
#
# time = input('enter time :').lower()
#
# if time == "утро" or time == "morning":
#     print("доброе утро !")
# elif time == "день" or time == "day":
#     print("добрый день !")
# elif time == "вечер" or time == "evening":
#     print("добрый вечер !")
# else:
#     print("Здравстуйте! (время суток неизвестно))")
#
#
# mon = float(input("""Cколько вы потратели ???
# [за Понидельник]: """))
# tue = float(input("""Cколько вы потратели ???
# [за Вторник]: """))
# wed = float(input("""Cколько вы потратели ???
# [за Среду]: """))
# thu = float(input("""Cколько вы потратели ???
# [за Чертверк]: """))
# fri = float(input("""Cколько вы потратели ???
# [за Пятницу]: """))
# sat = float(input("""Cколько вы потратели ???
# [за Субботу]: """))
# sun = float(input("""Cколько вы потратели ???
# [за Воскрисения] """))
#
# totalSum = mon + tue + wed + thu + fri + sat + sun
# totalSum = round(totalSum, 1)
#
# average = totalSum / 7
# average = round(average, 1)
#
# print(f'общая сумма потраченных денег за неделю : {totalSum} cомов')
# print(f'также средняя сумма потраченных денег {average} сомов')
#
#
# if totalSum >= 1 and totalSum <= 100:
#     print('потрачено мало')
# elif totalSum > 101 and totalSum <= 500:
#     print("потрачено нормально")
# elif totalSum > 501:
#     print("потрачено много")
# else:
#     print("не было трат")
#
# temerature = int(input("enter temperature: "))
#
# if temerature >= -30 and temerature <= 0:
#     print("холодно")
# elif temerature >= 1 and temerature <= 15:
#     print("прохладно")
# elif temerature >= 16 and temerature <= 26:
#     print("тепло")
# elif temerature >= 26 and temerature <= 40:
#     print("жарко")
# else:
#     print(f'несовмистимая с жиснью температура - {temerature} ')
