import math
#task
# counter = 0
# a, b = int(input()), int(input())
# for i in range(a, b +1):
#     if i % 10 == 4 or i % 10 == 9:
#         counter += 1
# print(counter)

#next_task
# n = int(input())
# total = 0
# for _ in range(1, n + 1):
#     num = int(input())
#     total += num
# print(total)

#next_task
# num1 = 0
# n_1 = int(input())
# for i in range(1, n_1):
#     num1 = num1 + (1 / (i + 1))
# num2 = num1 + 1 - math.log(n_1)
# print(num2)

#next_task
# total_1 = 0
# n_2 = int(input())
# for i in range(1, n_2 + 1):
#     if i**2 % 10 == 2 or i**2 % 10 == 5 or i**2 % 10 == 8:
#         total_1 += i
# print(total_1)

#next_task
# n_3 = int(input())
# n_3 = math.factorial(n_3)
# print(n_3)

#next_task
# total_2 = 1
# for i in range(1, 11):
#     num_3 = int(input())
#     if num_3 > 0:
#         total_2 *= num_3
# print(total_2)

#next_task
# n_4 = int(input())
# total_sum = 0
# for i in range(1, n_4 + 1):
#     if n_4 % i == 0:
#         total_sum += i
# print(total_sum)

#next_task
# n_5 = int(input())
# res = 0
# for i in range(1, n_5 + 1):
#     if i % 2 == 0:
#         res -= i
#     elif i % 2 != 0:
#         res += i
# print(res)

#next_task
n6 = int(input())
largest = 0
prelargest = 0
for i in range(1, n6 + 1):
    num4 = int(input())
    if num4 > largest:
        prelargest = largest
        largest = num4
    elif num4 > prelargest:
        prelargest = num4
print(largest)
print(prelargest)



