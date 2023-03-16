import jsonpickle

from Domain.piesa import Piesa
from Repository.json_repository import JsonRepository


class PiesaService:
    def __init__(self, producatorRepository: JsonRepository,
                 piesaRepository: JsonRepository):
        self.piesaRepository = piesaRepository
        self.producatorRepository = producatorRepository

    def adauga(self, id, nume, col, pret, idP,):
        """adauga un obiect de tip piesa"""
        if nume == "":
            raise KeyError("Numele trebuie sa nu fie nul.")
        if self.producatorRepository.read(idP) is None:
            raise KeyError("Id-ul prod nu e bun")
        piesa = Piesa(id, nume, col, pret, idP)
        self.piesaRepository.create(piesa)

    def afsOrdo(self, para):
        """ordo alfabetic a pieselor cu pretul mai mare decat o valoare //
        am atasat colectia separat ca sa fie usor de observata ordinea alfabetica"""
        lista = []
        for piesa in self.piesaRepository.read():
            if piesa.pret > para:
                lista.append({
                    "piesa": self.piesaRepository.read(piesa.id_entity),
                    "din colectia de": piesa.colectie
                })
        return sorted(lista, key=lambda rez: rez["din colectia de"])

    def afsOrdoNume(self):
        """afisarea pieselor de moblier ordonate dupa nume, alaturi de numele producatorilor"""
        lista = []
        for piesa in self.piesaRepository.read():
            if piesa.colectie == "dormitor":
                prod = self.producatorRepository.read(piesa.idProd)
                lista.append({
                    "nume piesa": piesa.nume,
                    "producatorii": prod.nume
                })
        return sorted(lista, key=lambda prod: prod['nume piesa'])

    def exportJson(self, filename):
        """export json a celor cerute"""
        lista = {}

        for prod in self.producatorRepository.read():
            lista[prod.nume] = []
            o2 = []
            oList = []
            nrP = 0
            sP = 0
            for piesa in self.piesaRepository.read():
                if piesa.idProd == prod.id_entity:
                    nrP += 1
                    sP = sP + piesa.pret
                    oList.append(piesa.nume)
            o2.append({
                "numarPieseMobilier": nrP,
                "sumaPret": sP,
                "piese": oList
            })
            lista[prod.nume].append(o2)
        with open(filename, 'w') as f:
            f.write(jsonpickle.dumps(lista))
