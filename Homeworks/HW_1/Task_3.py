# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

start_num = 2
finish_num = 10
middle = (finish_num + start_num) // 2

for i in range(start_num, finish_num+1):
    for j in range(start_num, middle):
        print(f'{j} * {i:2} = {i * j:2}', end='\t\t')
    print()
print()
for i in range(start_num, finish_num + 1):
    for j in range(middle, finish_num, 1):
        print(f'{j} * {i:2} = {i * j:2}', end='\t\t')
    print()