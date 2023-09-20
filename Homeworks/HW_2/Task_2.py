# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. \
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions


from math import gcd
from fractions import Fraction


def get_float_numbers(fraction_string: str):
    split = fraction_string.split("/")
    return int(split[0]), int(split[1])


first_fraction = input("first fraction = ")
second_fraction = input("second fraction = ")
try:
    a, b = get_float_numbers(first_fraction)  # a / b
    c, d = get_float_numbers(second_fraction)  # c / d
except (IndexError, ValueError):
    print("Input correct data!")
    exit()
ac = a * c
bd = b * d
divider_for_product = gcd(ac, bd)
numerator = a * d + c * b
divider_for_sum = gcd(bd, numerator)
print(f"Sum = {int(numerator / divider_for_sum)}/{int(bd / divider_for_sum)} vs " +
      f"{Fraction(first_fraction) + Fraction(second_fraction)}")
print(f"Product = {int(ac / divider_for_product)}/{int(bd / divider_for_product)} vs " +
      f"{Fraction(first_fraction) * Fraction(second_fraction)}")

