import math


def logarithm(value, base=math.e):
    """
    Обчислює логарифм числа 'value' за основою 'base'.

    :param value: Число, для якого обчислюється логарифм (повинно бути більше нуля).
    :param base: Основа логарифму (за замовчуванням e — натуральний логарифм).
    :return: Значення логарифму.
    """
    if value <= 0:
        raise ValueError("Аргумент 'value' повинен бути більше нуля")
    if base <= 0 or base == 1:
        raise ValueError("Основа логарифму повинна бути більше нуля і не дорівнювати 1")

    return math.log(value, base)
