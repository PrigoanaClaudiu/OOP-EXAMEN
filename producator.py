from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Producator(Entity):
    """creeaza o clasa de tipul producator"""
    nume: str
    email: str
