# Clínica Veterinaria

Mini proyecto desarrollado en Python para el examen de recuperación.

## Datos del estudiante

- Nombre: Jesús Armando Cavazos Castillo
- Matrícula: 2330175
- Grupo: 8-1
- Variante: 05 — Clínica veterinaria

## Descripción

Este proyecto implementa un sistema de consola para administrar las mascotas registradas en una clínica veterinaria.

Permite registrar, consultar, modificar y eliminar mascotas, además de realizar operaciones como calcular el peso promedio, filtrar mascotas por especie y encontrar la mascota de mayor edad.

## Funcionalidades

El sistema permite:

- Registrar mascotas.
- Mostrar todas las mascotas registradas.
- Buscar una mascota mediante su ID.
- Actualizar los datos de una mascota.
- Eliminar mascotas.
- Evitar identificadores duplicados.
- Validar los datos introducidos.
- Calcular el peso promedio de las mascotas.
- Filtrar mascotas por especie.
- Encontrar la mascota de mayor edad.
- Mostrar un resumen general.
- Manejar entradas incorrectas sin finalizar el programa.

## Datos de una mascota

Cada mascota contiene:

- ID.
- Nombre.
- Especie.
- Edad.
- Peso.

## Estructura del proyecto

```text
recuperacion-python-2330175/
│
├── .gitignore
├── .python-version
├── README.md
├── pyproject.toml
├── uv.lock
│
├── src/
│   └── recuperacion_python_2330175/
│       ├── __init__.py
│       ├── main.py
│       ├── models.py
│       └── services.py
│
└── tests/
    ├── __init__.py
    └── test_services.py