# Sistema de Ventas Python

Sistema de ventas para tienda de barrio construido como proyecto de aprendizaje en Python.

## Funcionalidades

- **Ver inventario**: lista productos con precio, cantidad y estado (agotado/disponible)
- **Hacer una venta**: seleccionar productos, validar stock, generar ticket con IVA (19%)
- **Ver ventas totales**: historial de todas las ventas realizadas
- **Reponer stock**: agregar unidades a productos existentes
- **Crear producto**: agregar nuevos productos al inventario con validación de datos

## Tecnologías

- Python 3.10
- pandas (práctica de análisis de datos)

## Estructura del proyecto

```
tienda.py                          # Sistema de ventas (proyecto principal)
proyecto_grande_tienda.py          # Versión inicial (práctica de diccionarios)
tienda_sin_funciones.py            # Versión sin funciones (referencia)
ventas.csv                         # Datos de ejemplo para pandas
pandas1_leer.py                    # Ejercicio de lectura CSV con pandas
Dia 1/                             # Ejercicios: strings, listas, zip, sets
Dia 2/                             # Ejercicios: inventario con for
Dia 3/                             # Ejercicios: if, for, while, break
dia 4/                             # Ejercicios: funciones, try/except
```

## Cómo ejecutar

```bash
python tienda.py
```

## Conceptos aplicados

- Diccionarios anidados
- Funciones con `def` y `return`
- Control de flujo: `if/elif/else`, `for`, `while`
- `try/except` para validación de entrada
- `break`, `continue`, `while True`
- `enumerate()`, f-strings, comprensión de sets
