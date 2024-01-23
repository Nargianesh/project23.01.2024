import evidence
from evidence import Evidence
from pojistenec import Pojistenec

print("________________________")
print("__Evidence pojistenych__")
print("________________________")

databaza = evidence.Evidence()

while True:
    print("\nVyberte si akci:")
    print("1 - Přidat nového pojištěného")
    print("2 - Vypsat všechny pojištěné")
    print("3 - Vyhledat pojistného podle jména a příjmení")
    print("4 - Konec")

    akce =int(input())

    if akce==1:
        jmeno=input("Zadejte jméno pojištence: ")
        prijmeni=input("Zadejte přijmení: ")
        vek=input("Zadejte věk: ")
        telefon=input("Zadejte telefonní číslo: ")

        databaza.pridej_osobu(jmeno, prijmeni, vek, telefon)

    elif akce == 2:
        databaza.zobraz_pojistene()

    elif akce == 3:
        jmeno = input("Zadejte jméno pojištence: ")
        prijmeni = input("Zadejte přijmeni pojištence:")

        databaza.hledej_osobu(jmeno, prijmeni)

    elif akce == 4:
        print("Konec aplikace")
        break

    else:
        print("Výberte akce JEN mezí 1-4 ")












