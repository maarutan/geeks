data_tuple = ("h", 6.13, "C", "e", "T", True, "k", "e", 3, "e", 1, "g")

letters = []
numbers = []
letters1 = []

for i in data_tuple:
    if isinstance(i, str):
        letters1.append(i)
    elif isinstance(i, bool):
        letters1.append(i)
    elif isinstance(i, int):
        numbers.append(i)


3, 2, 1


numbers[1:1] = [2]
numbers.sort()


for i in range(len(numbers)):
    numbers[i] = numbers[i] ** 2


boolion = bool

for i in letters1:
    if isinstance(i, bool):
        boolion = i


letters.append(boolion)

for i in letters1:
    if isinstance(i, str):
        letters.append(i)


letters[1] = "G"
letters[7] = "c"

a = tuple(letters)
b = tuple(numbers)

print(a)
print(b)
