vowelsCyrillic = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
vowelsLatin = "aeiouAEIOU"

exits = ["выход", "exit"]
while True:
    letters = input("(exit/выход) ввидите слово: ")
    if letters.lower() in exits:
        break

    totalLetter = 0
    vovels = 0
    noVovels = 0

    for i in letters:
        if i.isalpha():
            totalLetter += 1
        if i in vowelsLatin or i in vowelsCyrillic:
            vovels += 1
        else:
            noVovels += 1

    if totalLetter == 0:
        print("вы не ввели нечего ввидите от (А/Я) или (A/Z)")
        continue

    Vsum = round((vovels / totalLetter) * 100, 2)
    noVsum = round((noVovels / totalLetter) * 100, 2)

    print(f"\nСлово: {letters}")
    print("-----------------")
    print(f"Количество букв: {totalLetter}")
    print(f"Гласных букв: {vovels}")
    print(f"Согласных букв: {noVovels}")
    print(f"Гласные/Согласные: {Vsum}% / {noVsum}%\n")
