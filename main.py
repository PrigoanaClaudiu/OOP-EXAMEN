from Repository.json_repository import JsonRepository
from Service.piesaService import PiesaService
from Service.producatorService import ProducatorService
from UserInterface.consola import Consola


def main():
    producatorRepository = JsonRepository("prod.json")
    piesaRepository = JsonRepository("piesa.json")

    producatorService = ProducatorService(producatorRepository)
    piesaService = PiesaService(producatorRepository, piesaRepository)
    consola = Consola(producatorService, piesaService)
    consola.runMenu()


if __name__ == '__main__':
    main()
