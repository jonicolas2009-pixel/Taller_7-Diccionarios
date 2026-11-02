# Taller_7-Diccionarios
ACTIVIDAD GUIADA 1: Gestión de inventario

1. Tipo de dato de claves y valores
Las claves son de tipo str (cadenas de texto: "cuaderno", "lapiz", "borrador"). Los valores son de tipo int (números enteros: 12, 30, 8).

2. Consulta segura de “reglas”
Con inventario.get("reglas", 0) el resultado es 0. La clave "reglas" todavía no existe, y get() devuelve el valor por defecto (0) en lugar de lanzar un KeyError como pasaría con inventario["reglas"].

3. Agregar “regla” con valor 10
inventario["regla"] = 10. Como la clave no existía, Python la crea. El diccionario queda con 4 elementos.

4. Modificar “cuaderno” a 15
inventario["cuaderno"] = 15. Como la clave ya existía, Python reemplaza el valor anterior (12) por 15.

5. Suma total de existencias
sum(inventario.values()) da 63, porque 15 + 30 + 8 + 10 = 63
