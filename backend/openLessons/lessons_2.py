while True:
    try:
        n1 = float(input("1 число: "))
        action = input("действие: ")
        n2 = float(input("2 число: "))

        if action == "+":
            answer = n1 + n2
            print(answer)

        elif action == "-":
            answer = n1 - n2
            print(answer)

        elif action == "*":
            answer = n1 * n2
            print(answer)

        elif action == "/":
            answer = n1 / n2
            print(answer)
        else:
            print("неправильное действие !!!!")
    except:
        print("введити число")
