def add(a, b):
    """Soma dois números."""
    return a + b

def subtract(a, b):
    """Subtrai dois números."""
    return a - b

def multiply(a, b):
    """Multiplica dois números."""
    return a * b

def divide(a, b):
    """Divide dois números, retorna None se o divisor for zero."""
    if b == 0:
        return None
    return a / b

def is_positive(number):
    """Verifica se um número é positivo."""
    return number > 0