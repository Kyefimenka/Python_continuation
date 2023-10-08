# cоздайте функцию генератор чисел Фибоначчи

def fibonacci(n):
    num1 = 1
    num2 = 0
    next_number = num1
    count = 1

    while count <= n:
        yield next_number
        count += 1
        num1, num2 = num2, next_number
        next_number = num1 + num2


for number in fibonacci(10):
    print(number, end=" ")
