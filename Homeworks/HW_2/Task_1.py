# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное \
# строковое представление. Функцию hex используйте для проверки своего результата.

def get_hex_digit(code):
    if 0 <= code <= 9:
        return str(code)
    else:
        alphabet = "ABCDEF"
        return alphabet[code - 10]


num = int(input("input a number: "))
hex_num = hex(num)
digits = ''
while num > 0:
    rest = num % 16
    digits += get_hex_digit(rest)
    num = num // 16
print(f"{digits[::-1]} vs {hex_num}")
