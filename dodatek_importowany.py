import os
#kolor = "\033[0;32m"
#end = "\033[0m"
#print(f"{kolor}załadowano biblioteke 1.0 {end}")
def zaladuj_dodatek(zmienna = False):
    if zmienna == True:
        return "Wersja DI: 1.1"
    else:
        return "owoc"

Y = zaladuj_dodatek()
def czyszczenie_ekranu():
    os.system("cls")
    i = 10
    for i in range(1, 10):
        pass
def funkcja_pytania():
    global Y
    zmienna = str(input(f"podaj {Y}: "))
    return zmienna.lower()
def sprawdz(nazwa, lista):
    global Y
    if nazwa in lista:
        nazwa.upper()
        a = "oraz występuje " + str(lista.count(nazwa)) + " razy"
        return "taki " + Y + " jak: " + '"' + nazwa + '"' + " istnieje na liście " + a
    else:
        nazwa.upper()
        return "przepraszamy, taki " + Y + " jak: " + '"' + nazwa + '"' + " NIE istnieje na liście"
def usun(nazwa, lista):
    global Y
    if nazwa in lista and not nazwa.isdigit():
        lista.remove(nazwa)
        print(f"{Y} został pomyślnie usunięty, {lista}")
        return lista
    elif nazwa.isdigit() is True:
        nazwa = int(nazwa)
        if nazwa > 0 and nazwa < len(lista):
            print(len(lista))
            nazwa = nazwa - 1
            lista.pop(nazwa)
            print(f"{Y} został pomyślnie usunięty, {lista}")
            return lista
        else:
            print(f"ERROR! [02] taki {Y} nie istnieje")
    else:
        print(f"ERROR! [03] taki {Y} nie istnieje")

def dodaj(nazwa, lista,od_przodu = False):
    global Y
#   if nazwa.isdigit() is False and nazwa.isalpha():
    if od_przodu == True:
        lista.insert(0, nazwa)
        print(f"pomyślnie dodano {Y}: {nazwa}, {lista}")
        return lista
    elif nazwa.isalpha():
        lista.append(nazwa)
        print(f"pomyślnie dodano {Y}: {nazwa}, {lista}")
        return lista
    else:
        print(f"ERROR! [04] taki {Y} nie istnieje")
def popraw(nazwa, lista):
    global Y
    nowa_nazwa = input("Podaj nową nazwe: ")
    lista[(lista.index(nazwa))] = nowa_nazwa
    print(f"pomyślnie zastąpiono {Y}: {nowa_nazwa}, {lista}")
    return lista

def zamien(nazwa, lista):
    global Y
    nazwa2 = input(f"podaj drugą nazwe {Y}: ")
    # nazwa = mango/1, nazwa2 = kiwi/2
    if nazwa in lista:
        nazwa = lista.index(nazwa)
    elif nazwa.isdigit() is True:
        nazwa = int(nazwa)
        if nazwa > 0 and nazwa < len(lista):
            print(len(lista))
            nazwa = nazwa - 1
        else:
            print("error")
    else:
        print("error")
    if nazwa2 in lista:
        nazwa2 = lista.index(nazwa2)
    elif nazwa2.isdigit() is True:
        nazwa2 = int(nazwa2)
        if nazwa2 > 0 and nazwa2 < len(lista):
            print(len(lista))
            nazwa2 = nazwa2 - 1
        else:
            print("error")
    else:
        print("error")
    tmp = lista[nazwa]
    lista[nazwa] = lista[nazwa2]
    lista[nazwa2] = tmp
    print(f"Zamiana zakończona powodzeniem, {lista}")
    return lista

