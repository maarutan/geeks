vowelsCyrillic = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
vowelsLatin = "aeiouAEIOU"

while True:
    letter = input("('выход/exit' для выхода)\nВведите свое слово: ")
    if letter.lower() in "exit" or letter.lower() in "выход":
        break

    totalLetter = 0
    vowels = 0
    novowels = 0

    for char in letter:
        if char.isalpha():
            totalLetter += 1
        if char in vowelsLatin or char in vowelsCyrillic:
            vowels += 1
        else:
            novowels += 1

    if totalLetter == 0:
        print("Вы не ввели букв. Пожалуйста, введите только буквы (А-Я) или (A-Z)")
        continue

    vowelsSum = round((vowels / totalLetter) * 100, 2)
    novowelsSum = round((novowels / totalLetter) * 100, 2)

    print(f"\nСлово: {letter}")
    print("-----------------")
    print(f"Количество букв: {totalLetter}")
    print(f"Гласных букв: {vowels}")
    print(f"Согласных букв: {novowels}")
    print(f"Гласные/Согласные: {vowelsSum}% / {novowelsSum}%\n")
