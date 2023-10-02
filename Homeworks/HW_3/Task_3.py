# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.*Верните все возможные варианты комплектации рюкзака.
import random

supplies = {
    "burner": 0.5,
    "sleeping_bag": 1,
    "tent": 4,
    "food": 5,
    "cloth": 1,
    "water": 3,
    "light": 0.5,
    "dishes": 3,
   }
backpack_weight = float(input("Input the weight of the backpack: "))
backpack = []

backpack2 = []
supplies2 = supplies.copy()
backpack_weight2 = backpack_weight

isFound = True
while isFound:
    isFound = False
    for name in list(supplies.keys()):
        if supplies[name] <= backpack_weight:
            backpack.append(name)
            backpack_weight -= supplies[name]
            del supplies[name]
            isFound = True
            break

for _ in range(1000):
    if not any(supplies2):
        break
    name = random.choice(list(supplies2.keys()))
    if supplies2[name] <= backpack_weight2:
        backpack2.append(name)
        backpack_weight2 -= supplies2[name]
        del supplies2[name]

print(backpack)
print(backpack2)
