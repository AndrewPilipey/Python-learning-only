import math
#task
x_1, y_1, x_2, y_2 = float(input()), float(input()), float(input()), float(input())
euclidean_distance = math.sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)
print(euclidean_distance)


#next_task
r = float(input())
S = math.pi * r ** 2
C = 2 * math.pi * r
print(S)
print(C)


#next_task
num_1, num_2 = float(input()), float(input())
arithmetic_mean = (num_1 + num_2) / 2
geometric_mean = math.sqrt(num_1 * num_2)
harmonic_mean = (2 * num_1 * num_2) / (num_1 + num_2)
root_mean_square = math.sqrt((num_1**2 + num_2**2) / 2)
print(arithmetic_mean)
print(geometric_mean)
print(harmonic_mean)
print(root_mean_square)


#next_task
x_d = float(input())
x_r = math.radians(x_d)
x_final = math.sin(x_r) + math.cos(x_r) + math.tan(x_r)**2
print(x_final)


#next_task
x_f_c = float(input())
x_f_c = math.ceil(x_f_c) + math.floor(x_f_c)
print(x_f_c)


#next_task
a, b, c = float(input()), float(input()), float(input())
D = b**2 - 4*a*c
if D < 0:
    print("Нет корней")
elif D == 0:
    print(-b / (2*a))
elif D > 0:
    x_11 = (-b - math.sqrt(D)) / (2*a)
    x_22 = (-b + math.sqrt(D)) / (2*a)
    print(min(x_11, x_22))
    print(max(x_11, x_22))


#next_task
n_p, a_p = int(input()), float(input())
S_polygon = (n_p * a_p**2) / (4 * math.tan(math.pi / n_p))
print(S_polygon)

print("test")
print("test")