from dataclasses import dataclass


@dataclass
class Mascota:
    """Representa una mascota registrada en la clínica veterinaria."""

    id: str
    nombre: str
    especie: str
    edad: int
    peso: float