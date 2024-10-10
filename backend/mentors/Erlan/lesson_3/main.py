"""операторы назначение операторы пренадлежности, цикл while, for"""
from time import sleep
# userInput = input("enter number: ")

# int - что это
# int() - что это 


# name = "marat"
# surname = "arzymatov"

# print("1")
# print("\nname: ", name,"\nsurname:",surname,"\n")
# print("2")
# print("\nname:" + " " + name + " " + "\nsuraname: "+surname)
# print("3")
# print("name: {} surame: {}".format(surname,name))
# print("4")
# print(f"name: {name} surame: {surname}")


"""
написать 

инпут а
инпут b 
 
 это все число

a + b 
каторая присваевается в result 
a отоборажалось в 
b отоборажалось в 

то что должно быть в print()
вы ввили a вы ввили b рузультат result
"""

# a = int(input('\nВведите число а: '))
# b = int(input('Введите число б: '))

# result = a + b 
# print('-------------------')
# print(f"Вы ввели число: {a}\nВы ввели число: {b}\nРезультат: {result}\n")


# counter = 1
# while counter < 51:
#     print(f'hello({counter})')
#     sleep(.1)
#     counter += 1

   
# counter2 = 0
# while counter2 < 51:
#     sleep(0.1)
#     if counter2 == 40:
#         counter2 += 1
#         continue

#     print(f'hello2({counter2})')
#     counter2 += 1


    
# love =  0
# while love < 101:
#     print(f"({love}) детка прости меня ❤️")
#     sleep(.1)
#     love += 1
    
# for i in range(11):
#     print(f"({i}) sorry baby")
#     sleep(.1)
    
# count = 1
# while count <= 50:
#     print(f'hello ({count})') 
#     sleep(.1)
#     count += 1
    
    


# cyrillic = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
# latin = "aeiouAEIOU"

# exits = "выход exit"

# while True :
#     letters = input("enter your word: ")

#     totalLetter = 0
#     noVal = 0 
#     val = 0

#     if letters in exits :
#         break

#     for let in letters:
#         if let.isalpha():
#             totalLetter += 1
#             if let in latin or let in cyrillic:
#                 val += 1
#             else:
#                 noVal += 1
#         if totalLetter == 0 :
#             print("вы не ввели слово")  
#             continue


#     volSum = round((val / totalLetter) * 100, 2)
#     noVolSum = round((noVal / totalLetter) * 100, 2)

#     print(f"\nСлово: {letters}")
#     print("-----------------")
#     print(f"Количество букв: {totalLetter}")
#     print(f"Гласных букв: {val}")
#     print(f"Согласных букв: {noVal}")
#     print(f"Гласные/Согласные: {volSum}% / {noVolSum}%\n")


import os 
print(os.path.dirname(__file__))   