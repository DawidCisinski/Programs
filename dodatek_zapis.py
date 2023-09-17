import os
def zaladuj_dodatek_zapis(zmienna = False):
    if zmienna == True:
        return "Wersja DZ: 1.1"
    else:
        return "error"
def wczytaj():
    if os.path.exists("zapis_bin.txt"):
        with open("zapis_bin.txt", "r") as plik:
            lista = eval(plik.read())
        return lista
    else:
        return ["jabłko", "gruszka", "banan", "kiwi", "pomarańcza"]
def zapisz(lista):
    with open("zapis_bin.txt", "w") as plik:
        plik.write(str(lista))
    print(f"zapisano liste: {lista}")