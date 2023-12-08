import re

def palabras_minusculas(texto):
    # Utiliza la función findall para encontrar todas las palabras con letras minúsculas
    patron = re.compile(r'\b[a-z]+\b')
    return patron.findall(texto)

# Ejemplo de uso
texto_ejemplo = "Esta es una prueba de Texto con Palabras Minúsculas."
palabras_encontradas = palabras_minusculas(texto_ejemplo)
print("Palabras con letras minúsculas:", palabras_encontradas)
