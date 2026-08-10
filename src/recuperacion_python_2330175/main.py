"""Programa principal del sistema de clínica veterinaria."""

from .models import Mascota
from .services import (
    actualizar_mascota,
    buscar_mascota,
    calcular_peso_promedio,
    eliminar_mascota,
    filtrar_por_especie,
    obtener_mascota_mayor_edad,
    obtener_resumen,
    registrar_mascota,
)


def mostrar_mascota(mascota: Mascota) -> None:
    """Muestra los datos de una mascota."""
    print(f"\nID: {mascota.id}")
    print(f"Nombre: {mascota.nombre}")
    print(f"Especie: {mascota.especie}")
    print(f"Edad: {mascota.edad} años")
    print(f"Peso: {mascota.peso:.2f} kg")


def leer_edad() -> int:
    """Solicita una edad válida."""
    while True:
        try:
            edad = int(input("Edad: "))

            if edad < 0:
                print("La edad no puede ser negativa.")
                continue

            return edad
        except ValueError:
            print("La edad debe ser un número entero.")


def leer_peso() -> float:
    """Solicita un peso válido."""
    while True:
        try:
            peso = float(input("Peso en kg: "))

            if peso <= 0:
                print("El peso debe ser mayor que cero.")
                continue

            return peso
        except ValueError:
            print("El peso debe ser un número.")


def registrar(mascotas: list[Mascota]) -> None:
    """Solicita los datos y registra una mascota."""
    print("\n--- Registrar mascota ---")

    mascota_id = input("ID: ").strip()
    nombre = input("Nombre: ").strip()
    especie = input("Especie: ").strip()
    edad = leer_edad()
    peso = leer_peso()

    mascota = Mascota(
        mascota_id,
        nombre,
        especie,
        edad,
        peso,
    )

    try:
        resultado = registrar_mascota(mascotas, mascota)

        if resultado:
            print("\nMascota registrada correctamente.")
        else:
            print("\nYa existe una mascota con ese ID.")

    except (ValueError, TypeError) as error:
        print(f"\nError: {error}")


def mostrar_todas(mascotas: list[Mascota]) -> None:
    """Muestra todas las mascotas registradas."""
    print("\n--- Mascotas registradas ---")

    if not mascotas:
        print("No hay mascotas registradas.")
        return

    for mascota in mascotas:
        mostrar_mascota(mascota)


def buscar(mascotas: list[Mascota]) -> None:
    """Busca y muestra una mascota."""
    print("\n--- Buscar mascota ---")

    mascota_id = input("ID de la mascota: ").strip()
    mascota = buscar_mascota(mascotas, mascota_id)

    if mascota is None:
        print("No se encontró una mascota con ese ID.")
        return

    mostrar_mascota(mascota)


def actualizar(mascotas: list[Mascota]) -> None:
    """Solicita nuevos datos para una mascota."""
    print("\n--- Actualizar mascota ---")

    mascota_id = input("ID de la mascota: ").strip()

    if buscar_mascota(mascotas, mascota_id) is None:
        print("No se encontró una mascota con ese ID.")
        return

    nombre = input("Nuevo nombre: ").strip()
    especie = input("Nueva especie: ").strip()
    edad = leer_edad()
    peso = leer_peso()

    try:
        resultado = actualizar_mascota(
            mascotas,
            mascota_id,
            nombre,
            especie,
            edad,
            peso,
        )

        if resultado:
            print("Mascota actualizada correctamente.")
        else:
            print("No se pudo actualizar la mascota.")

    except (ValueError, TypeError) as error:
        print(f"Error: {error}")


def eliminar(mascotas: list[Mascota]) -> None:
    """Elimina una mascota solicitando su ID."""
    print("\n--- Eliminar mascota ---")

    mascota_id = input("ID de la mascota: ").strip()

    if eliminar_mascota(mascotas, mascota_id):
        print("Mascota eliminada correctamente.")
    else:
        print("No se encontró una mascota con ese ID.")


def mostrar_peso_promedio(mascotas: list[Mascota]) -> None:
    """Muestra el peso promedio."""
    if not mascotas:
        print("\nNo hay mascotas registradas.")
        return

    promedio = calcular_peso_promedio(mascotas)
    print(f"\nPeso promedio: {promedio:.2f} kg")


def mostrar_por_especie(mascotas: list[Mascota]) -> None:
    """Filtra y muestra mascotas por especie."""
    especie = input("\nEspecie a buscar: ").strip()
    resultado = filtrar_por_especie(mascotas, especie)

    if not resultado:
        print("No se encontraron mascotas de esa especie.")
        return

    print(f"\n--- Mascotas de especie {especie} ---")

    for mascota in resultado:
        mostrar_mascota(mascota)


def mostrar_mayor_edad(mascotas: list[Mascota]) -> None:
    """Muestra la mascota con mayor edad."""
    mascota = obtener_mascota_mayor_edad(mascotas)

    if mascota is None:
        print("\nNo hay mascotas registradas.")
        return

    print("\n--- Mascota de mayor edad ---")
    mostrar_mascota(mascota)


def mostrar_resumen(mascotas: list[Mascota]) -> None:
    """Muestra un resumen general."""
    resumen = obtener_resumen(mascotas)

    print("\n--- Resumen general ---")
    print(f"Total de mascotas: {resumen['total_mascotas']}")
    print(f"Peso promedio: {resumen['peso_promedio']:.2f} kg")


def mostrar_menu() -> None:
    """Muestra las opciones disponibles."""
    print("\n================================")
    print("     CLÍNICA VETERINARIA")
    print("================================")
    print("1. Registrar mascota")
    print("2. Mostrar mascotas")
    print("3. Buscar mascota")
    print("4. Actualizar mascota")
    print("5. Eliminar mascota")
    print("6. Calcular peso promedio")
    print("7. Filtrar mascotas por especie")
    print("8. Mostrar mascota de mayor edad")
    print("9. Mostrar resumen general")
    print("0. Salir")


def main() -> None:
    """Ejecuta el menú principal del programa."""
    mascotas: list[Mascota] = []

    while True:
        mostrar_menu()

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            registrar(mascotas)
        elif opcion == "2":
            mostrar_todas(mascotas)
        elif opcion == "3":
            buscar(mascotas)
        elif opcion == "4":
            actualizar(mascotas)
        elif opcion == "5":
            eliminar(mascotas)
        elif opcion == "6":
            mostrar_peso_promedio(mascotas)
        elif opcion == "7":
            mostrar_por_especie(mascotas)
        elif opcion == "8":
            mostrar_mayor_edad(mascotas)
        elif opcion == "9":
            mostrar_resumen(mascotas)
        elif opcion == "0":
            print("\nPrograma finalizado.")
            break
        else:
            print("\nOpción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
