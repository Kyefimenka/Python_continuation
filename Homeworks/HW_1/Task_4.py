# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c — \
# стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других. \
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами \
# не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

a = 6
b = 6
c = 6

if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        message = " the triangle is equilateral"
    elif a == b or b == c or a == c:
        message = " the triangle is isosceles"
    else:
        message = " the triangle is versatile"
else:
    message = " such a triangle does not exist"
print(message)