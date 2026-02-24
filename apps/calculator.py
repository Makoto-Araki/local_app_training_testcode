def divide(a, b):
    return a / b

def divide_custom(a, b):
    if b == 0:
        raise ValueError('zero divide is forbidden')
    return a / b
