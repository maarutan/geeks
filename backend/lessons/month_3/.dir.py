import os

userName = input("Enter your name: ")

for i in range(1, 9):
    name = f"lesson_{i}"
    os.makedirs(name, exist_ok=True)
    pathFile = os.path.join(name, "main.py")
    with open(pathFile, "w") as file:
        welcomeFile = f'"Welcome {userName} to lesson {i}"'
        file.write(welcomeFile)
