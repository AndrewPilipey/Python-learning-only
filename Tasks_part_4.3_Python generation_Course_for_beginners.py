n, k = int(input()), int(input()) #n - Zoom, k - Flash
if n > k:
    print("NO")
elif k > n:
    print("YES")
else:
    print("Don't know")

#next_task
side_a, side_b, side_c = int(input()), int(input()), int(input())
if side_a == side_b == side_c:
    print("Равносторонний")
elif side_a == side_b or side_a == side_c or side_b == side_c:
    print("Равнобедренный")
else:
    print("Разносторонний")

#next_task
a, b, c = int(input()), int(input()), int(input())
if b < a < c or b > a > c:
    print(a)
elif a < b < c or a > b > c:
    print(b)
else:
    print(c)

#next_task
month = int(input())
if month in (1, 3, 5, 7, 8, 10, 12):
    print(31)
elif month in (4, 6, 9, 11):
    print(30)
else:
    print(28)

#next_task
weight_category = int(input())
if weight_category < 60:
    print("Легкий вес")
elif 60 <= weight_category < 64:
    print("Первый полусредний вес")
elif 64 <= weight_category < 69:
    print("Полусредний вес")

#next_task
number_1 = int(input())
number_2 = int(input())
sign = input()
if sign == "+":
    print(number_1 + number_2)
elif sign == "-":
    print(number_1 - number_2)
elif sign == "*":
    print(number_1 * number_2)
elif sign == "/":
    if number_2 == 0:
        print("На ноль делить нельзя!")
    else:
        print(number_1 / number_2)
else:
    print("Неверная операция")

#next_task
color_1 = input()
color_2 = input()
if "красный" in (color_1, color_2) and "синий" in (color_1, color_2):
    print("фиолетовый")
elif "красный" in (color_1, color_2) and "желтый" in (color_1, color_2):
    print("оранжевый")
elif "синий" in (color_1, color_2) and "желтый" in (color_1, color_2):
    print("зеленый")
elif "красный" in color_1 or "синий" in color_1 or "желтый" in color_1 and color_1 == color_2:
    print(color_1)
else:
    print("ошибка цвета") #некорректное решение через in. Понял это потом.
                        #Корректно решать через оператор сравнения ==.

