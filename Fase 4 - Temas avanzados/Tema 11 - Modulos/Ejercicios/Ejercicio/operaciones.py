def suma(a,b):
    try:
        r = a + b
    except TypeError:
        print('ERROR, tipo de dato no válido')
    else:
        return r


def resta(a,b):
    try:
        r = a - b
    except TypeError:
        print('ERROR, tipo de dato no válido')
    else:
        return r


def producto(a,b):
    try:
        r = a * b
    except TypeError:
        print('ERROR, tipo de dato no válido')
    else:
        return r


def division(a,b):
    try:
        r = a / b
    except TypeError:
        print('ERROR, tipo de dato no válido')
    except ZeroDivisionError:
        print('ERROR, no es posible dividir entre 0')
    else:
        return r