"""Даны три целых числа. Найти количество положительных чисел в исходном наборе."""
# count = 0
# number1 = int(input('Введите первое число: '))
# number2 = int(input('Введите второе число: '))
# number3 = int(input('Введите третье число: '))
# if number1 > 0:
#     count += 1
# if number2 > 0:
#     count += 1
# if number3 > 0:
#     count +=1
# print(f'Количество положительных чисел: {count}')
# a, b, = [int(input('Введите: ')) for _ in range(2)]
'''Даны два числа. Вывести большее из них.'''
# n1, n2 = int(input('Введите первое число: ')), int(input('Введите второе число: '))
# if n1 > n2:
#     print('Наибольшее число:', n1)
# elif n2 > n1:
#     print('Наибольшее число:', n2)
# else:
#     print('Числа равны')
'''Даны два числа. Вывести вначале большее, а затем меньшее из них.'''
# try:
#     n1, n2 = int(input('Введите первое число: ')), int(input('Введите второе число: '))
#     if n1 > n2:
#         max_n = n1
#         min_n = n2
#     else:
#         max_n = n2
#         min_n = n1
#     print('Максимальное число', max_n)
#     print('Минимальное число', min_n)
# except ValueError:
#     print('Не корректный ввод')
'''Даны три числа. Найти наименьшее из них.'''
# n1, n2 = int(input('Введите первое число: ')), int(input('Введите второе число: ')),
# n3 = int(input('Введите третье число: '))
# if n1 < n2 and n1 < n3:
#     print('Наименьшее число:', n1)
# elif n2 < n3 and n2 < n1:
#     print('Наименьшее число:', n2)
# else:
#     print('Наименьшее число:', n3)
'''Даны координаты точки, не лежащей на координатных осях OX и OY.
Определить номер координатной четверти, в которой находится данная точка.
Координаты задаются пользователем, например (10, 15).'''
# x = float(input('X = '))
# y = float(input('Y = '))
# if x > 0 and y > 0:
#     print('№ четверти 1')
# elif x < 0 and y < 0:
#     print('№ четверти 3')
# elif x > 0 > y:
#     print('№ четверти 2')
# elif x < 0 < y:
#     print('№ четверти 4')
# else:
#     print('Точка на оси, или в центре координат!')