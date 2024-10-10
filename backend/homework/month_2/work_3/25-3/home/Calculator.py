class Calculator:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Calculator(self.value + other.value)

    def __sub__(self, other):
        return Calculator(self.value - other.value)

    def __mul__(self, other):
        return Calculator(self.value * other.value)

    def __truediv__(self, other):
        if other.value != 0:
            return Calculator(self.value / other.value)
        else:
            raise ValueError("Деление на ноль невозможно")

    def __str__(self):
        return str(self.value)

calc1 = Calculator(10)
calc2 = Calculator(5)

result_add = calc1 + calc2
print(result_add)

result_sub = calc1 - calc2
print(result_sub)

result_mul = calc1 * calc2
print(result_mul)

result_div = calc1 / calc2
print(result_div)
