#task
# a_leg_of_triangle = float(input())
# b_lef_of_triangle =  float(input())
# s_of_triangle = 0.5 * (a_leg_of_triangle * b_lef_of_triangle)
# print(s_of_triangle)

#next_task
# distance = float(input())
# speed_of_grandma_1 = float(input())
# speed_of_grandma_2 = float(input())
# print(distance / (speed_of_grandma_1 + speed_of_grandma_2))

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