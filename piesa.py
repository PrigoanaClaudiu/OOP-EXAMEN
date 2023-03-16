from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Piesa(Entity):
    """creeaza o clasa de tipul piesa"""
    nume: str
    colectie: str
    pret: int
    idProd: str
