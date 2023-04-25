#topic: variables

number = 3
number2 = 5
result = number + number2
print(result)

num1 = num2 = 10
print(num1, num2)

num_1, num_2, num_3 = 1, 2, 3
print(num_1, num_2, num_3)

swap1, swap2 = 99, 66
swap1, swap2 = swap2, swap1  + swap2
print(swap1, swap2)

swap2 = swap2 - number #(this is as same as: swap2 -= number)
print(swap2)

#распаковка списка по переменным:
z, x, c = [11, 22, 33]
print(z, x, c)
print(z)
print(x)
print(c)

z, x, *c = [11, 22, 33]
print(z, x, c)
print(z)
print(x)
print(c)
