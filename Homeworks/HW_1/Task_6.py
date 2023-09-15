#Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. /
#Программа должна подсказывать «больше» или «меньше» после каждой попытки.

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
TRIALS = 10
num = randint(LOWER_LIMIT, UPPER_LIMIT)

for i in range(TRIALS+1):
    number = int(input("What a number have I wished?: "))
    if number > num:
        message = "my number is smaller than yours"
    elif number < num:
        message = "my number is bigger than yours"
    else:
        message = f"you won! I have wished {num}"
        print(message)
        exit()
    print(message)
message = "you lost!"
print(message)


