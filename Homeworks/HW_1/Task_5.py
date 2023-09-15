# Напишите код, который запрашивает число и сообщает является ли оно простым или составным. \
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу и на себя».\
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

LOWER_LIMIT = 1
UPPER_LIMIT = 100000
while True:
    number = input(f"Input a number between {LOWER_LIMIT} and {UPPER_LIMIT}: ")
    if number.isdecimal() and LOWER_LIMIT <= int(number) <= UPPER_LIMIT:
        break
number = int(number)
count = 0
for i in range(2, number // 2+1):
    if number % i == 0:
        count += 1
if count != 0:
    print("this number isn't simple")
else:
    print("this number is simple")