mon = float(input("""Cколько вы потратели ???
[за Понидельник]: """))
tue = float(input("""Cколько вы потратели ???
[за Вторник]: """))
wed = float(input("""Cколько вы потратели ???
[за Среду]: """))
thu = float(input("""Cколько вы потратели ???
[за Чертверк]: """))
fri = float(input("""Cколько вы потратели ???
[за Пятницу]: """))
sat = float(input("""Cколько вы потратели ???
[за Субботу]: """))
sun = float(input("""Cколько вы потратели ???
[за Воскрисения] """))

totalSum = mon + tue + wed + thu + fri + sat + sun
totalSum = round(totalSum, 1)

average = totalSum / 7
average = round(average, 1)

print(f'общая сумма потраченных денег за неделю : {totalSum} cомов')
print(f'также средняя сумма потраченных денег {average} сомов')


if totalSum >= 1 and totalSum <= 100:
    print('потрачено мало')
elif totalSum > 101 and totalSum <= 500:
    print("потрачено нормально")
elif totalSum > 501:
    print("потрачено много")
else:
    print("не было трат")
