#
# def describe_number(number):
#     if 100 <= number <= 999:
#         hundreds = ['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
#         tens = ['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
#         ones = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
#         teens = ['', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать',
#                  'семнадцать', 'восемнадцать', 'девятнадцать']
#
#         hundreds_digit = number // 100
#         tens_digit = (number % 100) // 10
#         ones_digit = number % 10
#
#         match number:
#             case _ if number == 100:
#                 return 'сто'
#             case _ if 110 <= number <= 119:
#                 return f'{hundreds[hundreds_digit]} {teens[number - 110]}'
#             case _:
#                 return f'{hundreds[hundreds_digit]} {tens[tens_digit]} {ones[ones_digit]}'
#     else:
#         return 'Число не входит в диапазон от 100 до 999'
# number = int(input('Введите число (100 до 999): '))
# print(f"{number} — '{describe_number(number)}'")

""" Реализуйте программу калькулятор. На вход подается три значения: первое число,
второе число и операция( *, /, + или -) . На выходе должны получить число, после выполнения операции."""


# def calculate(first_operand, second_operand, operation):
#     match operation:
#         case '*':
#             return first_operand * second_operand
#         case '/':
#             return first_operand / second_operand
#         case '+':
#             return first_operand + second_operand
#         case '-':
#             return first_operand - second_operand
#
#
# try:
#     first_number = float(input('Введите первое число: '))
#     second_number = float(input('Введите второе число: '))
#     operation = input('Введите операцию (*, /, +, -): ')
#
#     result = calculate(first_number, second_number, operation)
#     print(f'Результат: {result}')
# except ValueError:
#     print('Ошибка: Некорректный формат числа. Пожалуйста, введите числа заново.')
# except ZeroDivisionError:
#     print('Деление на ноль не допустимо!')
