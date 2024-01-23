from pojistenec import Pojistenec
class Evidence():
    def __init__(self):
        self.pojistene = []

    def pridej_osobu(self, jmeno, prijmeni, vek, telefon):
        if not jmeno :
            print("Error:jmeno nemate přidane")
        elif not prijmeni:
            print("Error.Musíte zadát přijmeni")
            return
        pojistenec = Pojistenec(jmeno, prijmeni, vek, telefon)
        self.pojistene.append(pojistenec)
        print(f"Udaje {jmeno} {prijmeni} pojištené osoby bylá uložená ")

    def zobraz_pojistene(self):
        if not self.pojistene:
            print("Zatim nemáte žádne udaje uložené")
        else:
            for pojistenec in self.pojistene:
                print (f" {pojistenec.jmeno}  {pojistenec.prijmeni}")

    def hledej_osobu (self, jmeno, prijmeni):
        for pojistenec in self.pojistene:
            if pojistenec.jmeno==jmeno and pojistenec.prijmeni==prijmeni:
                print("Pojištenec byl nálezen v naší databazi ")
            else:
                print("Pojištenec nebyl nálezen")







