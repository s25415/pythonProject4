from os import system
from random import random, randint


def zad1():
    arr = input("Podaj liczby: ").replace(' ', '').split(',')
    min = arr[0]
    max = arr[0]
    for arg in arr:
        if min > arg:
            min = arg
        if max < arg:
            max = arg
    print("MIN = " + min)
    print("MAX = " + max)

def zad2():
    arr1 = ["Warszawa", "Kraków", "Łudź", "Wrocław", "Poznań", "Gdańsk",
            "Szczecin", "Bydgoszcz", "Lublin", "Białystok"]
    arr2 = []
    for i in range(0, randint(1,10)):
        arr2.append(arr1.pop(randint(0,9-i)))
    for arg in arr2:
        print(arg)

def zad3():
    iloscRund = int(input("Ile rund? "))
    gracze = int(input("Ilu graczy(1-2)? "))
    while gracze not in range(1,3):
        gracze = int(input("Błąd, podaj poprawnie liczbę graczy graczy(1-2)? "))
    gracz1 = input("Podaj nazwę gracza 1: ")

    gracz2 = "Komputer"
    if gracze == 2 :
        gracz2= input("Podaj nazwę gracza 2: ")

    wynik1=0
    wynik2=0
    for i in range(1, iloscRund+1):
        akcja1 = int(input(gracz1 + ": Kamień(1), papier(2), czy nożyce(3)?"))
        system('cls')
        if gracze == 2:
            akcja2 = int(input(gracz2 + ": Kamień(1), papier(2), czy nożyce(3)?"))
            system('cls')
        else :
            akcja2 = randint(1,3)
            match akcja2:
                case 1:
                    print("Komputer: Kamień")
                case 2:
                    print("Komputer: Papier")
                case 3:
                    print("Komputer: Nożyce")
        if akcja1 == 1 and akcja2 == 2 or akcja1 == 2 and akcja2 == 3 or akcja1 == 3 and akcja2 == 1:
            wynik2+=1
        if akcja2 == 1 and akcja1 == 2 or akcja2 == 2 and akcja1 == 3 or akcja2 == 3 and akcja1 == 1:
            wynik1 += 1

    system('cls')
    print("Koniec")
    print(gracz1 + ": " + str(wynik1)+" punktów")
    print(gracz2 + ": " + str(wynik2)+" punktów")
    if wynik1 > wynik2:
        print("Wygrywa "+ gracz1)
    else :
        if wynik1 < wynik2:
            print("Wygrywa " + gracz2)
        else:
            print("Remis")

if __name__ == '__main__':
    zad3()

