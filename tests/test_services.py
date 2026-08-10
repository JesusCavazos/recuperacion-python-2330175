import pytest

from recuperacion_python_2330175.models import Mascota
from recuperacion_python_2330175.services import (
    actualizar_mascota,
    buscar_mascota,
    calcular_peso_promedio,
    eliminar_mascota,
    filtrar_por_especie,
    obtener_mascota_mayor_edad,
    registrar_mascota,
)


def test_registrar_mascota():
    mascotas = []
    mascota = Mascota("M001", "Firulais", "Perro", 5, 12.5)

    resultado = registrar_mascota(mascotas, mascota)

    assert resultado is True
    assert len(mascotas) == 1


def test_buscar_mascota_existente():
    mascotas = [
        Mascota("M001", "Firulais", "Perro", 5, 12.5),
    ]

    resultado = buscar_mascota(mascotas, "M001")

    assert resultado is not None
    assert resultado.nombre == "Firulais"


def test_buscar_mascota_inexistente():
    mascotas = [
        Mascota("M001", "Firulais", "Perro", 5, 12.5),
    ]

    resultado = buscar_mascota(mascotas, "M999")

    assert resultado is None


def test_no_permitir_id_duplicado():
    mascotas = [
        Mascota("M001", "Firulais", "Perro", 5, 12.5),
    ]

    nueva = Mascota("M001", "Michi", "Gato", 3, 4.0)

    resultado = registrar_mascota(mascotas, nueva)

    assert resultado is False
    assert len(mascotas) == 1


def test_rechazar_edad_negativa():
    mascotas = []
    mascota = Mascota("M002", "Michi", "Gato", -2, 4.0)

    with pytest.raises(ValueError):
        registrar_mascota(mascotas, mascota)


def test_rechazar_peso_negativo():
    mascotas = []
    mascota = Mascota("M003", "Rocky", "Perro", 4, -5.0)

    with pytest.raises(ValueError):
        registrar_mascota(mascotas, mascota)


def test_calcular_peso_promedio():
    mascotas = [
        Mascota("M001", "Firulais", "Perro", 5, 10.0),
        Mascota("M002", "Michi", "Gato", 3, 20.0),
    ]

    resultado = calcular_peso_promedio(mascotas)

    assert resultado == 15.0


def test_peso_promedio_lista_vacia():
    resultado = calcular_peso_promedio([])

    assert resultado == 0.0


def test_filtrar_por_especie():
    mascotas = [
        Mascota("M001", "Firulais", "Perro", 5, 12.5),
        Mascota("M002", "Michi", "Gato", 3, 4.0),
        Mascota("M003", "Luna", "Gato", 7, 5.0),
    ]

    resultado = filtrar_por_especie(mascotas, "Gato")

    assert len(resultado) == 2
    assert all(mascota.especie == "Gato" for mascota in resultado)


def test_obtener_mascota_mayor_edad():
    mascotas = [
        Mascota("M001", "Firulais", "Perro", 5, 12.5),
        Mascota("M002", "Michi", "Gato", 9, 4.0),
    ]

    resultado = obtener_mascota_mayor_edad(mascotas)

    assert resultado is not None
    assert resultado.nombre == "Michi"


def test_actualizar_mascota():
    mascotas = [
        Mascota("M001", "Firulais", "Perro", 5, 12.5),
    ]

    resultado = actualizar_mascota(
        mascotas,
        "M001",
        "Firulais Junior",
        "Perro",
        6,
        13.0,
    )

    assert resultado is True
    assert mascotas[0].nombre == "Firulais Junior"
    assert mascotas[0].edad == 6


def test_eliminar_mascota():
    mascotas = [
        Mascota("M001", "Firulais", "Perro", 5, 12.5),
    ]

    resultado = eliminar_mascota(mascotas, "M001")

    assert resultado is True
    assert mascotas == []