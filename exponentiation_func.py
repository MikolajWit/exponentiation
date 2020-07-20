def exponentiation(base, exponent):
    if exponent == 0:
        return 1
    if base == 0 and exponent < 0:
        raise ZeroDivisionError
    if base == 0:
        return 0

    if base > 0 and exponent > 0:
        result = base
        for n in range(exponent - 1 ):
            result *= base
        return result

    if base < 0 and exponent < 0:
        result = 1/base
        for n in range(-exponent - 1):
            result /= base
        return result

    if base < 0 and exponent > 0:
        result = base
        for n in range(exponent - 1):
            result *= base
        return result


