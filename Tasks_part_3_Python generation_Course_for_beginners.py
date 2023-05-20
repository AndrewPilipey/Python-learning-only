#task
your_seat = int(input())
print((your_seat - 1) // 4 + 1)

#next_task
minutes = int(input())
print(minutes, "мин - это", minutes // 60, "час", minutes % 60, "минут.")

#next_task
enter_number = int(input())
sum_number = (enter_number % 10) + ((enter_number % 100) // 10) + (enter_number // 100)
print(sum_number)
multiplication_number = (enter_number % 10) * ((enter_number % 100) // 10) * (enter_number // 100)
print(multiplication_number)

#next_task
# Перестановка цифр
# Дано трехзначное число abc, в котором все цифры различны. Напишите программу, которая выводит шесть чисел, образованных при перестановке цифр заданного числа.
# Формат входных данных
# На вход программе подаётся положительное трёхзначное целое число, все цифры которого различны.
# Формат выходных данных
# Программа должна вывести шесть чисел, образованных при перестановке цифр заданного числа в следующем порядке:
# abc,acb,bac,bca,cab,cba.
abc = int(input())
a = abc // 100
b = (abc // 10) % 10
c = abc % 10
print(a, b, c, sep="")
print(a, c, b, sep="")
print(b, a, c, sep="")
print(b, c, a, sep="")
print(c, a, b, sep="")
print(c, b, a, sep="")

#next_task
abcd = int(input())
a = abcd // 1000
b = (abcd // 100) % 10
c = (abcd // 10) % 10
d = abcd % 10
print("Цифра в позиции тысяч равна", a)
print("Цифра в позиции сотен равна", b)
print("Цифра в позиции десятков равна", c)
print("Цифра в позиции единиц равна", d)

#next_task
abcde = 12345
print(abcde // 10000)
print(abcde % 10000 // 1000)
print(abcde % 1000 // 100)
print(abcde % 100 // 10)
print(abcde % 10)
