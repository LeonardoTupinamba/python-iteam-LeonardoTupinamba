import math


def area_circulo(raio):
    """
    Calcula a área de um círculo dado o raio.

    Args:
        raio (float): O raio do círculo.

    Returns:
        float: A área do círculo (π × r²).

    Example:
        >>> area_circulo(5)
        78.53981633974483
    """
    return math.pi * raio ** 2


def volume_esfera(raio):
    """
    Calcula o volume de uma esfera dado o raio.

    Args:
        raio (float): O raio da esfera.

    Returns:
        float: O volume da esfera ((4/3) × π × r³).

    Example:
        >>> volume_esfera(3)
        113.09733552923254
    """
    return (4 / 3) * math.pi * raio ** 3


def hipotenusa(cateto_a, cateto_b):
    """
    Calcula a hipotenusa de um triângulo retângulo dado os dois catetos.

    Args:
        cateto_a (float): O primeiro cateto.
        cateto_b (float): O segundo cateto.

    Returns:
        float: A hipotenusa (√(a² + b²)).

    Example:
        >>> hipotenusa(3, 4)
        5.0
    """
    return math.sqrt(cateto_a ** 2 + cateto_b ** 2)