def es_numero(valor):
    return isinstance(valor, (int, float))

def sumar(a, b):
    if es_numero(a) and es_numero(b):
        return a + b
    else:
        raise ValueError("Ambos parámetros deben ser números enteros o decimales.")

def restar(a, b):
    if es_numero(a) and es_numero(b):
        return a - b
    else:
        raise ValueError("Ambos parámetros deben ser números enteros o decimales.")

def multiplicar(a, b):
    if es_numero(a) and es_numero(b):
        resultado = 0
        for _ in range(abs(int(b))):
            resultado += a if b > 0 else -a
        return resultado
    else:
        raise ValueError("Ambos parámetros deben ser números enteros o decimales.")


def dividir(valor1, valor2):
    """
    Divide dos valores y retorna el resultado.
    """
    # Verificar que los valores sean int o float
    if not (isinstance(valor1, (int, float)) and isinstance(valor2, (int, float))):
        raise ValueError("Ambos valores deben ser de tipo int o float")

    # Verificar que el divisor no sea cero
    if valor2 == 0:
        raise ValueError("El divisor no puede ser cero")

    # Inicializar el resultado
    resultado = 0

    # Restar iterativamente valor2 a valor1 hasta que valor1 sea menor que valor2
    while valor1 >= valor2:
        valor1 -= valor2
        resultado += 1

    return resultado