# Арифметические операции
# Напишите программу, в которой вычисляется сумма, разность и произведение
# двух целых чисел, введенных с клавиатуры.
# 
# Формат входных данных
# На вход программе подаётся два целых
# числа, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести сумму, разность
# и произведение введённых чисел, каждое на отдельной строке.
#
# Тестовые данные 🟢
# Sample Input:
# 2
# 7
# Sample Output:
# 2 + 7 = 9
# 2 - 7 = -5
# 2 * 7 = 14
x = int(input())
y = int(input())

print(x, '+', y, '=', x + y)
print(x, '-', y, '=', x - y)
print(x, '*', y, '=', x * y)

#next_task
a_1 = int(input())
d = int(input())
n = int(input())

a_n = a_1 + d * (n - 1)
print(a_n)

#next_task
o = int(input())
print(o, o * 2, o * 3, o * 4, o * 5, sep='---')

next_task
b_1 = int(input())
q = int(input())
n = int(input())
print(b_1 * q ** (n - 1))

next_task
centimeters = int(input())
meters = centimeters // 100
print(meters)

next_task
students = int(input())
mandarins = int(input())

print(mandarins // students)
print(mandarins % students)

next_task
population_of_universe = int(input())
print((population_of_universe // 2) + (population_of_universe % 2))

next_task
