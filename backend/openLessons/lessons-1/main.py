import random
import os
from time import sleep


botCount = 0
userCount = 0


knb = ["rock", "paper", "scissors"]
ext = ["exit", "back", "close"]
while True:
    try:
        usrI = input("/ rock / paper / scissors /\nenter: ")
        bot = random.choice(knb)
        print("-----------------------------")

        if usrI in ext:
            print(knb)
            os.system("clear")
            print(
                """
        /)＿/)☆
     ／(๑^᎑^๑)っ ＼
    |￣∪￣  ￣|＼／
    |＿＿_＿＿|／
                          _ _      
 _  _ ___ _  _   _____ _(_) |_ ___
| || / _ \ || | / -_) \ / |  _(_-<
 \_, \___/\_,_| \___/_\_\_|\__/__/
 |__/                             
                  """
            )
            break

        if usrI == "rock" and bot == "paper":
            os.system("clear")
            print("you: rock vs bot: paper\n \nbot won!!!\n")
            botCount += 1
            sleep(1)

        elif usrI == "rock" and bot == "scissors":
            os.system("clear")
            print("you: rock vs bot: scissors\n \nyou won!!!\n")
            userCount += 1
            sleep(1)

        elif usrI == "rock" and bot == "rock":
            os.system("clear")
            print("you: rock vs bot: rock\n \ndraw !!!\n")
            sleep(1)

        elif usrI == "paper" and bot == "scissors":
            os.system("clear")
            print("you: rock vs bot: scissors\n \nbot won!!!\n")
            botCount += 1
            sleep(1)

        elif usrI == "paper" and bot == "rock":
            os.system("clear")
            print("you: rock vs bot: rock\n \nyou won !!!\n")
            userCount + 1
            sleep(1)

        elif usrI == "paper" and bot == "paper":
            os.system("clear")
            print("you: rock vs bot: rock\n \ndraw !!!\n")
            sleep(1)

        elif usrI == "scissors" and bot == "scissors":
            os.system("clear")
            print("you: scissors vs bot: scissors\n \ndraw !!!\n")
            userCount + 1
            sleep(1)

        elif usrI == "scissors" and bot == "rock":
            os.system("clear")
            print("you: scissors vs bot: rock\n \nbot won !!!\n")
            botCount + 1
            sleep(1)

        elif usrI == "scissors" and bot == "paper":
            os.system("clear")
            print("you: scissors vs bot: scissors\n \you won !!!\n")
            sleep(1)
    except KeyboardInterrupt:
        os.system("clear")
        print("вы завершили")
        break
