# Задача №7 (Квадраты натуральных чисел)

"""
По данному целому числу N распечатайте все квадраты
натуральных чисел, не превосходящие N, в порядке возрастания.
"""

n = int(input('Введите целое число: '))
num = 0

for r in range(1, n+1):
    if r ** 2 > n:
        break
    num = r ** 2
    print(num)