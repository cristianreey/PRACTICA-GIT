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
