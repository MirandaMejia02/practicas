import re

def contiene_fecha_valida(cadena):
    # Utiliza la función search para buscar el formato de fecha en la cadena
    patron = re.compile(r'\b\d{2}/\d{2}/\d{4}\b')
    return bool(patron.search(cadena))

# Ejemplo de uso
texto_con_fechas = "La reunión será el 15/12/2022 y otra el 20/01/2023"
resultado_busqueda = contiene_fecha_valida(texto_con_fechas)
print(f"¿La cadena contiene al menos una fecha válida? {resultado_busqueda}")
