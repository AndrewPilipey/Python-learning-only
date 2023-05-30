#task
a_leg_of_triangle = float(input())
b_lef_of_triangle =  float(input())
s_of_triangle = 0.5 * (a_leg_of_triangle * b_lef_of_triangle)
print(s_of_triangle)

#next_task
distance = float(input())
speed_of_grandma_1 = float(input())
speed_of_grandma_2 = float(input())
print(distance / (speed_of_grandma_1 + speed_of_grandma_2))

#next_task
num = float(input())
if num == 0:
    print("Обратного числа не существует")
else:
    print(num**-1)

#next_task
fahrenheit = float(input())
celsius = 5/9 * (fahrenheit - 32)
print(celsius)

#next_task
dog_age = float(input())
if 1 <= dog_age <= 2:
    print(dog_age * 10.5)
else:
    print(2 * 10.5 + (dog_age - 2) * 4)

#next_task
piece = float(input())
piece = piece * 10 % 10
print(int(piece))

#next_task
fraction = float(input())
print(fraction - (fraction // 1))

#next_task
first, second, third, fourth, fifth = int(input()), int(input()), int(input()), int(input()), int(input())
print("Наименьшее число =", min(first, second, third, fourth, fifth))
print("Наибольшее число =", max(first, second, third, fourth, fifth))

#next_task
a, b, c = int(input()), int(input()), int(input())
print(max(a, b, c))
print((a + b + c) - min(a, b, c) - max(a, b, c))
print(min(a, b, c))

#next_task
interesting_num = int(input())
first_digit = interesting_num // 100
second_digit = interesting_num // 10 % 10
third_digit = interesting_num % 10
if (max(first_digit, second_digit, third_digit) - min(first_digit, second_digit, third_digit) ==
       (first_digit + second_digit + third_digit) - max(first_digit, second_digit, third_digit) -
        min(first_digit, second_digit,third_digit)):
    print("Число интересное")
else:
    print("Число неинтересное")

#next_task
a_1, a_2, a_3, a_4, a_5 = float(input()), float(input()), float(input()), float(input()), float(input())
print(abs(a_1) + abs(a_2) + abs(a_3) + abs(a_4) + abs(a_5))

#next_task
p_1, p_2, q_1, q_2 = int(input()), int(input()), int(input()), int(input())
manhattan_distance = abs(p_1 - q_1) + abs(p_2 - q_2)
print(manhattan_distance)