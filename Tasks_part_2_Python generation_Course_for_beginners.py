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