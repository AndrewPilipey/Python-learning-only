#Task_1
year = int(input())
last_digit_of_year = year % 10
penultimate_digit_of_the_year = year // 10 % 10
if last_digit_of_year == 0 and penultimate_digit_of_the_year == 0:
    print("YES")
else:
    print("NO")


#Task_2
column_1 = int(input())
line_1 = int(input())
column_2 = int(input())
line_2 = int(input())
if (column_1 + line_1) % 2 == 0 and (column_2 + line_2) % 2 == 0:
    print("YES")
elif (column_1 + line_1) % 2 != 0 and (column_2 + line_2) % 2 != 0:
    print("YES")
else:
    print("NO")


#Task_3
age = int(input())
sex = input()
if 10 <= age <= 15 and sex == "f":
    print("YES")
else:
    print("NO")

#Task_4
roman_numeral = int(input())
if roman_numeral == 1:
    print("I")
elif roman_numeral == 2:
    print("II")
elif roman_numeral == 3:
    print("III")
elif roman_numeral == 4:
    print("IV")
elif roman_numeral == 5:
    print("V")
elif roman_numeral == 6:
    print("VI")
elif roman_numeral == 7:
    print("VII")
elif roman_numeral == 8:
    print("VIII")
elif roman_numeral == 9:
    print("IX")
elif roman_numeral == 10:
    print("X")
else:
    print("ошибка")


#Task_5
conditions = int(input())
if conditions % 2 != 0:
    print("YES")
elif 2 <= conditions <= 5 and conditions % 2 == 0:
    print("NO")
elif 6<= conditions <= 20 and conditions %2 == 0:
    print("YES")
elif 20 < conditions and conditions % 2 == 0:
    print("NO")

#Task_6
x_1, y_1, x_2, y_2 = int(input()), int(input()), int(input()), int(input())
if (x_1 - x_2)**2 == (y_1 - y_2)**2:
    print("YES")
else:
    print("NO")

#Task_7
xh_1, yh_1, xh_2, yh_2 = int(input()), int(input()), int(input()), int(input())
if (xh_1 - xh_2) * (yh_1 - yh_2) == 2 or (xh_1 - xh_2) * (yh_1 - yh_2) == -2:
    print("YES")
else:
    print("NO")


#Task_8
xq_1, yq_1, xq_2, yq_2 = int(input()), int(input()), int(input()), int(input())
if (xq_1 - xq_2)**2 == (yq_1 - yq_2)**2:
    print("YES")
elif xq_1 == xq_2 or yq_1 == yq_2:
    print("YES")
else:
    print("NO")