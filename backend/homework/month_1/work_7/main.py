# ------- 1 задание -------

def naytiBlizkoeChislo(spisok, chislo):
    otsortSpisok = sorted(spisok, key=lambda x: abs(x - chislo))
    vernutChto = (chislo, otsortSpisok)
    return vernutChto

mojSpisok = [10, 2, 14, 4, 7]
moeChislo = 5
print(naytiBlizkoeChislo(mojSpisok, moeChislo))

# ------- 2 задание -------

def vybratChetnoe(spisok):
    chetnye = list(filter(lambda x: x % 2 == 0, spisok))
    return chetnye

chisla = [1, 2, 3, 4, 5, 6, 7, 8]
print(vybratChetnoe(chisla))

def kvadratChisel(spisok):
    kvadraty = list(map(lambda x: x ** 2, spisok))
    return kvadraty

chisla2 = [1, 2, 3, 4]
print(kvadratChisel(chisla2))

# ------- 3 задание -------

def poluchitElement(spisok):
    while True:
        try:
            print(""" 
 ____________________________
< написал код в мемном ввиде >
 ----------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/
                ||----- |
                ||     ||

                  """)
            index = int(input("Vvedite index: "))
            print(spisok[index])
        except IndexError:
            print(f"Nepravilniy index! Dostupnie indexi ot 0 do {len(spisok) - 1}")
        except ValueError:
            print("Index dolzhen bit chislom. Dlya vihoda nazmite Ctrl+C.")

spisok = [10, 20, 30, 40, 50]
poluchitElement(spisok)

