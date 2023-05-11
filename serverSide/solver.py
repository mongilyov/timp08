def quadraticSolver(a, b, c):
    D = b * b - 4 * a * c
    if (D < 0):
        return ("negative discriminant", 0)
    x1 = (-b + D ** 0.5) / (2 * a)
    x2 = (-b - D ** 0.5) / (2 * a)
    return (x1, x2)