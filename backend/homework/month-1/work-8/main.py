def guessNumber():
    low, high = 1, 100
    attempts = 0
    guesses = []

    print("[-=-=-=-=-=-=-=-=-=-=-=-=-=-=]")
    print("Загадайте число от 1 до 100.")
    print("[-=-=-=-=-=-=-=-=-=-=-=-=-=-=]")

    while True:
        guess = (low + high) // 2
        attempts += 1
        guesses.append(guess)

        print("\n('да', 'больше', 'меньше',)\n(yes, >, <,)")
        userInput = input().strip().lower()

        if userInput in ['да', 'yes']:
            print("_____________________________________________")
            print(f"Угадано число {guess} за {attempts} попыток.")
            with open("results.txt", "a") as file:
                file.write("""
 _____________________________
< ваш выбор """ + str(guess) + """ >
 -----------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/
                ||----- |
                ||     ||
                """)
                file.write(f"Количество попыток: {attempts}\n")
                file.write(f"Попытки: {guesses}\n\n")
            print("""
 _____________________________
< вы выбрали """ + str(guess) + """ >
 -----------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/
                ||----- |
                ||     ||
                """)
            break
        elif userInput in ['больше', '>']:
            low = guess + 1
        elif userInput in ['меньше', '<']:
            high = guess - 1
        else:
            print("Ответьте: 'да', 'больше', 'меньше'\nили\n(yes, >, <,)")


guessNumber()
