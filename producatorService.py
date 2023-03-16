from Domain.producator import Producator
from Repository.json_repository import JsonRepository


class ProducatorService:
    def __init__(self, producatorRepository: JsonRepository):
        self.producatorRepository = producatorRepository

    def adauga(self, id, nume, email):
        """creeaza un obiect de tipul producator"""
        if nume == "":
            raise KeyError("Numele trebuie sa nu fie nul.")
        producator = Producator(id, nume, email)
        self.producatorRepository.create(producator)
