from Service.piesaService import PiesaService
from Service.producatorService import ProducatorService


class Consola:
    def __init__(self, producatorService: ProducatorService,
                 piesaService: PiesaService):
        self.piesaService = piesaService
        self.producatorService = producatorService

    def runMenu(self):
        while True:
            print("1. Adauga un producator.")
            print("2. Adauga o piesa de mobilier.")
            print("3. Afisarea pieselor cu pretul mai mare decat o val"
                  "si ordo alfabetic dupa colectie.")
            print("4. Afisarea pieselor din colectia DORMITOR, ordonate "
                  "dupa nume, alaturi de producatori.")
            print("5. Export Json.")
            print("x. Iesire.")

            optiune = input("Dati optiunea: ")
            if optiune == "1":
                self.uiAdgProd()
            elif optiune == "2":
                self.uiAdgPiesa()
            elif optiune == "3":
                para = int(input("Dati valoarea (int): "))
                print(self.piesaService.afsOrdo(para))
            elif optiune == "4":
                print(self.piesaService.afsOrdoNume())
            elif optiune == "5":
                self.uiExportJ()
            elif optiune == "x":
                break
            else:
                input("Optiune invalida")

    def uiAdgProd(self):
        try:
            id = input("Dati id-ul: ")
            nume = input("Dati numele: ")
            email = input("Dati email-ul: ")

            self.producatorService.adauga(id, nume, email)
        except Exception as e:
            print(e)

    def uiAdgPiesa(self):
        try:
            id = input("Dati id-ul: ")
            nume = input("Dati numele: ")
            col = input("Dati colectia: ")
            pret = int(input("Dati pretul: "))
            idP = input("Dati id-ul producatorului: ")

            self.piesaService.adauga(id, nume, col, pret, idP)
        except Exception as e:
            print(e)

    def uiExportJ(self):
        try:
            filename = input("Dati numele fisierului (ceva.json): ")
            self.piesaService.exportJson(filename)
        except Exception as e:
            print(e)
