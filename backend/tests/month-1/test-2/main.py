def kalc(inp1: float, opr: str, inp2: float) -> float:
    """
    Выполняет арифметические операции.

    Параметры:
    inp1: Первое число.
    opr: Арифметический оператор ('+', '-', '*', '/', '//', '**', '%').
    inp2: Второе число.

    Возвращает:
    Результат операции.
    """
    try:
        if opr not in ["+", "-", "*", "/", "//", "**", "%"]:
            raise ValueError("Недопустимый оператор.")

        if opr == "+":
            return inp1 + inp2
        elif opr == "-":
            return inp1 - inp2
        elif opr in ["//", ":"]:
            if inp2 == 0:
                raise ZeroDivisionError("Деление на ноль!")
            return inp1 // inp2
        elif opr == "/":
            if inp2 == 0:
                raise ZeroDivisionError("Деление на ноль!")
            return inp1 / inp2
        elif opr == "*":
            return inp1 * inp2
        elif opr == "**":
            return inp1 ** inp2
        elif opr == "%":
            return inp1 % inp2

    except TypeError:
        raise TypeError("inp1 и inp2 должны быть числами.")


print(kalc(2, "+", 1))
print(kalc(20, "/", 2))
print(kalc(10, "//", 3))
print(kalc(2, "**", 3))
print(kalc(10, "%", 3))
print(kalc(10, "/", 0))

print("hello")
