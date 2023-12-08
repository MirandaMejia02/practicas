import re

def encontrar_ocurrencias(texto, palabra):
    # Utiliza la función finditer para obtener un iterador de objetos de coincidencia
    patron = re.compile(fr'\b{re.escape(palabra)}\b', re.IGNORECASE)
    return [match.span() for match in patron.finditer(texto)]

# Ejemplo de uso
texto_ejemplo_2 = "La función es un ejemplo de función para buscar funciones."
palabra_a_buscar = "función"
ocurrencias = encontrar_ocurrencias(texto_ejemplo_2, palabra_a_buscar)
print(f"Ubicaciones de la palabra '{palabra_a_buscar}': {ocurrencias}")
