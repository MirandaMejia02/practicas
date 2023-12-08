def suma_lista(lista):
    # Caso base: si la lista está vacía, la suma es 0
    if not lista:
        return 0
    else:
        # Caso recursivo: suma el primer elemento y llama a la función con el resto de la lista
        return lista[0] + suma_lista(lista[1:])

# Ejemplo de uso
mi_lista = [1, 2, 3, 4, 5]
resultado = suma_lista(mi_lista)
print(f"La suma de la lista {mi_lista} es: {resultado}")
