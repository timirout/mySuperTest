# Задача № 5 (Три математических класса)

"""
В школе решили набрать три новых математических класса. Так как занятия по математике
у них проходят в одно и то же время, было решено выделить кабинет для каждого класса
и купить в них новые парты. За каждой партой может сидеть не больше двух учеников.
Известно количество учащихся в каждом из трёх классов. Сколько всего нужно закупить парт
чтобы их хватило на всех учеников? Программа получает на вход три натуральных числа:
количество учащихся в каждом из трех классов.

Использовать только арифметические операторы. Оператор IF не понадобится.

Подсказка: используйте операторы //, % и +
"""

a = int(input('Введите количество учеников в первом классе: '))
b = int(input('Введите количество учеников в втором классе: '))
c = int(input('Введите количество учеников в третьем классе: '))

res = a // 2 + b // 2 + c // 2 + a % 2 + b % 2 + c % 2

print('Нужно закупить '+ str(res) +' парт(ы) для трёх классов.')