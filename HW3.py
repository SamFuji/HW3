

# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# list =['в', 'Д', 'а', 'о', 'п', 'б', 'а', 'р', 'Ы', 'ы', 'ж', 'й', 'р', ' ',  'а', 'в', 'д', 'е', 'л', 'ч', 'п', 'е', 'д', 'р', 'л', '!']
# for i in range(len(list)):
#     if i %2 != 0:
#         print(list[i], end=' ')
# print(' ')

# list =[int(x) for x in input('Введите числа через пробел: ').split(' ')]
# print(list)
# sum = 0
# for i in range(len(list)):
#     if i %2 != 0:
#         sum += list[i]
# print( sum ) 


# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# from random import randint

# numbers = [randint(1,10) for i in range(randint(1,5))]
# print(numbers)
# mult_nmbrs = []
# len_odd = int(len(numbers)/2)
# if len(numbers) %2 == 0:
#     for i in range(len_odd):
#         mult_nmbrs.append(numbers[i]*numbers[-i-1])
#     print(mult_nmbrs)
# else:
#     for i in range(len_odd+1):
#         mult_nmbrs.append(numbers[i]*numbers[-i-1])
#     print(mult_nmbrs)


# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# a = int(input('Введите число: '))  
# print(a)
# b = ()
# bin_str = []
# while a > 0:
#     b = (a %2)
#     print(b)
#     bin_str = (b)[::-1]
#     a /=2
# print(bin_str)       #не закончено!!!


# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
