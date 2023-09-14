# Пользователь вводит число от 1 до 999. Используя операции с числами сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

MIN_NUM = 1
MAX_NUM = 999

while True:
    data = input(f"Input a number between {MIN_NUM} and {MAX_NUM}: ")
    if data.isdecimal() and MIN_NUM <= int(data) <= MAX_NUM:
        break

data = int(data)
if data // 10 == 0:
    answer = f'You entered a digit {data} \n result = {data**2}'
elif data // 100 == 0:
    product_of_digits = (data // 10) * (data % 10)
    answer = f'You entered a two-digit-number {data} \n result = {product_of_digits}'
else:
    mirroring = int(str(data)[::-1])
    answer = f'You entered a three-digit-number {data} \n result = {mirroring}'

print(answer)



