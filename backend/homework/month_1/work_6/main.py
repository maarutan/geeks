moviesList = {
    "Django Unchained": {
        "John": 10,
        "Jack": 9
    },
    "Troy": {}
}


def findMovie(movieName):
    return movieName in moviesList


def addMovie(movieName):
    movieName = movieName.title()
    if findMovie(movieName):
        print("Этот фильм уже существует!")
    else:
        moviesList[movieName] = {}
        print("Фильм успешно добавлен")


def addRating(movieName, userName, rating):
    movieName = movieName.title()
    if not findMovie(movieName):
        print("\n!-!-!-!-!-!-!-!-!-!")
        print("Такого фильма не существует")
        print("!-!-!-!-!-!-!-!-!-!")
    else:
        if userName in moviesList[movieName]:
            print("\n!-!-!-!-!-!-!-!-!-!")
            print(
                "Этот пользователь уже оценил фильм !!!")
            print("!-!-!-!-!-!-!-!-!-!")
        elif rating < 0 or rating > 10:
            print("Оценка должна быть от 0 до 10.")
        else:
            moviesList[movieName][userName] = rating
            print(f"Оценка добавлена  {movieName}: {
                  userName} оценил его на {rating}")


def viewRatings():
    if not moviesList:
        print("\n!-!-!-!-!-!-!-!-!-!")
        print("Фильмы отсутствуют.")
        print("!-!-!-!-!-!-!-!-!-!")
        return

    for movie, ratings in moviesList.items():
        if ratings:
            avgRating = sum(ratings.values()) / len(ratings)
            print(f"{movie} имеет рейтинг {round(avgRating, 1)}")
        else:
            print(f"Рейтинг для фильма {movie} пока недоступен")


while True:
    print("\nВыберите команду:")
    print("1. Добавить фильм")
    print("2. Добавить рейтинг")
    print("3. Показать рейтинги")
    print("0. Выход")
    print("[-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=]")
    choice = input("Введите номер команды: ")

    if choice == "1":
        movieName = input("Введите название фильма: ")
        addMovie(movieName)

    elif choice == "2":
        movieName = input("Введите название фильма: ")
        userName = input("Введите ваше имя: ")
        try:
            rating = float(input("Введите вашу оценку (0-10): "))
            addRating(movieName, userName, rating)
        except ValueError:
            print("\n!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!")
            print("Пожалуйста, введите првильные число для оценки.")
            print("!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!")

    elif choice == "3":
        viewRatings()

    elif choice == "0":
        print("\n!-!-!-!-!-!-!-!-!-!")
        print("Программа завершена.")
        print("!-!-!-!-!-!-!-!-!-!")
        break

    else:
        print("\n!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!")
        print("Неверная команда!!!")
        print("!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!")
