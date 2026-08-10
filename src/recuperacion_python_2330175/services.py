"""Funciones de gestión para las mascotas de la clínica veterinaria."""

from .models import Mascota


def buscar_mascota(
    mascotas: list[Mascota],
    mascota_id: str,
) -> Mascota | None:
    """Busca una mascota por su identificador."""
    for mascota in mascotas:
        if mascota.id == mascota_id:
            return mascota

    return None


def validar_mascota(mascota: Mascota) -> None:
    """Valida que los datos de una mascota sean correctos."""
    if not mascota.id.strip():
        raise ValueError("El ID no puede estar vacío.")

    if not mascota.nombre.strip():
        raise ValueError("El nombre no puede estar vacío.")

    if not mascota.especie.strip():
        raise ValueError("La especie no puede estar vacía.")

    if not isinstance(mascota.edad, int):
        raise TypeError("La edad debe ser un número entero.")

    if mascota.edad < 0:
        raise ValueError("La edad no puede ser negativa.")

    if not isinstance(mascota.peso, (int, float)):
        raise TypeError("El peso debe ser un número.")

    if mascota.peso <= 0:
        raise ValueError("El peso debe ser mayor que cero.")


def registrar_mascota(
    mascotas: list[Mascota],
    mascota: Mascota,
) -> bool:
    """Valida y registra una mascota si su ID no está repetido."""
    validar_mascota(mascota)

    if buscar_mascota(mascotas, mascota.id) is not None:
        return False

    mascotas.append(mascota)
    return True


def mostrar_mascotas(mascotas: list[Mascota]) -> list[Mascota]:
    """Devuelve todas las mascotas registradas."""
    return mascotas


def actualizar_mascota(
    mascotas: list[Mascota],
    mascota_id: str,
    nombre: str,
    especie: str,
    edad: int,
    peso: float,
) -> bool:
    """Actualiza los datos de una mascota existente."""
    mascota = buscar_mascota(mascotas, mascota_id)

    if mascota is None:
        return False

    datos_actualizados = Mascota(
        mascota_id,
        nombre,
        especie,
        edad,
        peso,
    )

    validar_mascota(datos_actualizados)

    mascota.nombre = nombre
    mascota.especie = especie
    mascota.edad = edad
    mascota.peso = peso

    return True


def eliminar_mascota(
    mascotas: list[Mascota],
    mascota_id: str,
) -> bool:
    """Elimina una mascota mediante su identificador."""
    mascota = buscar_mascota(mascotas, mascota_id)

    if mascota is None:
        return False

    mascotas.remove(mascota)
    return True


def calcular_peso_promedio(mascotas: list[Mascota]) -> float:
    """Calcula el peso promedio de las mascotas registradas."""
    if not mascotas:
        return 0.0

    peso_total = sum(mascota.peso for mascota in mascotas)
    return peso_total / len(mascotas)


def filtrar_por_especie(
    mascotas: list[Mascota],
    especie: str,
) -> list[Mascota]:
    """Devuelve las mascotas que pertenecen a una especie."""
    return [
        mascota for mascota in mascotas if mascota.especie.lower() == especie.lower()
    ]


def obtener_mascota_mayor_edad(
    mascotas: list[Mascota],
) -> Mascota | None:
    """Devuelve la mascota de mayor edad."""
    if not mascotas:
        return None

    return max(mascotas, key=lambda mascota: mascota.edad)


def obtener_resumen(
    mascotas: list[Mascota],
) -> dict[str, int | float]:
    """Genera un resumen general de las mascotas registradas."""
    return {
        "total_mascotas": len(mascotas),
        "peso_promedio": calcular_peso_promedio(mascotas),
    }
