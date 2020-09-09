# Задача №4 (Школьники и яблоки)

"""
n школьников делят k яблок поровну, неделящийся остаток остается в корзинке.
Сколько яблок достанется каждому школьнику? Сколько яблок останется в корзинке?
Программа получает на вход числа n и k и должна вывести искомое количество яблок (два числа).

Использовать только арифметические операторы (Подсказка: понадобятся // и %)
"""

n = int(input('Введите количество школьников: '))
k = int(input('Введите количество яблок: '))

a = k // n
print('Каждому школьнику досталось по', a, 'яблок(а).')

b = k % n
if b > 0:
    print('В корзине осталось', b, 'яблок(а).')
else:
    print('В корзине не осталось яблок.')