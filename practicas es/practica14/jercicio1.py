import re

def es_codigo_empleado_valido(cadena):
    patron = re.compile(r'^EMP\d{3}$')
    return bool(patron.match(cadena))

codigo_empleado = "EMP123"
resultado_validacion = es_codigo_empleado_valido(codigo_empleado)
print(f"¿El código de empleado '{codigo_empleado}' es válido? {resultado_validacion}")
