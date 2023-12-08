def invertir_cadena(cadena):
    # Caso base: si la cadena está vacía, devuelve la cadena vacía
    if not cadena:
        return cadena
    else:
        # Caso recursivo: invierte el resto de la cadena y agrega el primer carácter al final
        return invertir_cadena(cadena[1:]) + cadena[0]

# Ejemplo de uso
mi_cadena = "Hola, mundo!"
resultado_inversion = invertir_cadena(mi_cadena)
print(f"La cadena invertida de '{mi_cadena}' es: '{resultado_inversion}'")
