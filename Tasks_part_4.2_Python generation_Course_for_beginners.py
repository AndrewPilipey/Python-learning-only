#task
diapason = int(input())
if 0 <= diapason <= 16:
    print("Принадлежит")
else:
    print("Не принадлежит")

#next_task
diaposon_2 = int(input())
if diaposon_2 <= -3 or diaposon_2 >= 7:
    print("Принадлежит")
else:
    print("Не принадлежит")

#next_task
diaposon_3 = int(input())
if -30 < diaposon_3 <= -2 or 25 >= diaposon_3 > 7:
    print("Принадлежит")
else:
    print("Не принадлежит")

#next_task
beautiful_number = int(input())
if 1000 <= beautiful_number <= 9999:
    if beautiful_number % 7 == 0 or beautiful_number % 17 == 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")

#next_task
side_1 = int(input())
side_2 = int(input())
side_3 = int(input())
if side_1 > 0 and side_2 > 0 and side_3 >0:
    if side_1 < side_2 + side_3 and side_2 < side_1 + side_3 and side_3 < side_1 + side_2:
        print("YES")
    else:
        print("NO")
else:
    print("NO")

#next_task
leap_year = int(input())
if leap_year % 4 == 0 and leap_year % 100 != 0 or leap_year % 400 == 0:
    print("YES")
else:
    print("NO")

#next_task
column_number_1 = int(input())
line_number_1 = int(input())
column_number_2 = int(input())
line_number_2 = int(input())
if column_number_1 == column_number_2 or line_number_1 == line_number_2:
    print("YES")
else:
    print("NO")

#next_task
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a-1 <= c <= a+1 and b-1 <= d <= b+1:
    print("YES")
else:
    print("NO")