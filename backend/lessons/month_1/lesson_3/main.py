###Операторы принадлежности, назначения, Циклы.

###Операторы: Назначения


# number = 5
# print(number)
# number += 5
# print(number)

# number = 5
# number += 5
# number **= 2
# number //=4
# number -= 15
# print(number)

### Операторы: придналежности

# word = "geeks"
# print('o' in word)
# print('g' in word)
# print('z' not in word)
# print('s' not in word)

### Циклы "While" "For"

# counter = 0
# while counter <= 50:
#     if counter == 40:
#         print("stop")
#         break
#     counter += 1
#     if counter % 2 == 0:
#         continue
#     print("GEEKS", counter)

# rounds = int(input("сколько кругов нужно ?  "))


# rounds = int(input('сколько кругов нужно? '))
# while rounds > 0:
#     time = input(f'enter time: ({rounds}) ').lower()
#     if time in 'exit stop выход':
#         break
#     if time =='утро' or time == 'morning':
#         print('доброе утро')
#     elif time == 'день' or time == 'day':
#         print("добрый день")
#     elif time == 'вечер ' or time == 'evening':
#         print("добрый вечер")
#     else:
#         print("здравствуйте! (время суток неизвестно)")
#     rounds -= 1

### Цикл For

word = "KYRGYZSTAN"

for letter in word:
    if letter == "S":
        break
    if letter in "YRZSAN":
        continue
    print(letter)
