def factorial(n):
    if n < 0:
        raise ValueError("Факторіал визначений тільки для невід'ємних чисел")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)