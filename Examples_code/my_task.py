"""
Введение

Рассмотрим первые 16 членов приведенного ниже ряда:

11,32,53,94,135,176,217,298,379,460,541,622,703,784,865,1026...

который генерируется этой последовательностью:

11,21,21,41,41,41,41,81,81,81,81,81,81,81,81,161....

Каждый член u последовательности получается путем нахождения последней степени 2 (или самого себя, если u является степенью 2) * 10 + 1.

Задача

Учитывая переменную n, вычислите nth член ряда, показанного выше.

Тесты

10 фиксированных тестов: первые 10 семестров
100 случайных тестов: 1e100 <n <1e101

Примечания:

Наивные решения не пройдут, поэтому не пытайтесь сгенерировать последовательность.
Стремитесь к сублинейному решению (постоянное время возможно, но не обязательно).
"""


def squared_digits_series(n):
    num = 1
    number = 0

    while n > 0:
        for j in range(num):
            n -= 1
            number += (num * 10) + 1
            if not n:
                break
        num *= 2
        if not n:
            break

    return number


print(squared_digits_series(10))