import decimal

STEP = 50
RATE = 0.015
L_LIMIT = 30
H_LIMIT = 600
RATE_THREE = 0.03
SUM_MAX = 5000000
RATE_W = 0.1
CMD_DEPOSIT = "d"
CMD_WITHDRAW = "w"
CMD_EXIT = "e"

deposit = 0
count = 0

while True:
    action = input(f"Пополнить - {CMD_DEPOSIT}, снять - {CMD_WITHDRAW}, выйти - {CMD_EXIT}. Введите команду: ")
    if action == CMD_EXIT:
        print(f"Заберите карту. На ней {deposit} у. е.")
        break
    if action in (CMD_DEPOSIT, CMD_WITHDRAW):
        amount = 1
        while amount % STEP != 0:
            amount = decimal.Decimal(input(f"Введите сумму кратную {STEP}: "))
        if action == CMD_DEPOSIT:
            count += 1
            deposit += amount
            result = f"Пополнение карты на {amount}. На карте {deposit} у. е."
            # if count % 3 == 0:
            #     deposit += RATE_THREE
            #     print(f"Начислено {RATE_THREE * 100} %. На карте {deposit} у. е.")
        else:
            count += 1
            percent = amount * decimal.Decimal(RATE)
            if percent < L_LIMIT:
                percent = L_LIMIT
            if percent > H_LIMIT:
                percent = H_LIMIT
            withdraw_sum = percent + amount
            if deposit >= withdraw_sum:
                deposit -= withdraw_sum
                result = f"Снятие с карты {amount}, комиссия за снятие {percent} у. е. На карте {deposit} у. е."
            else:
                result = f"Недостаточно средств"
        print(result)
        if count % 3 == 0:
            deposit += decimal.Decimal(RATE_THREE) * deposit
            print(f"Начислено {RATE_THREE * 100} %. На карте {deposit} у. е.")
        if deposit > SUM_MAX:
            percent = deposit * decimal.Decimal(RATE_W)
            deposit -= percent
            print(f"Вычтен налог на богатство: {RATE_W * 100} % в сумме {percent}. На карте {deposit} у. е.")
    else:
        print("Неверная команда")