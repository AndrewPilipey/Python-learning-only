answer = input("What programming language are we learning?\n")
if answer == "Python" or answer == "python":
    print("Yes, that's correct.")
else:
    print("Go away, you damn fool. We are learning Python.")

#task
password_1 = input()
password_2 = input()
if password_1 == password_2:
    print("Пароль принят")
else:
    print("Пароль не принят")

#next_task
entered_num = int(input())
if entered_num % 2 == 0:
    print("Четное")
else:
    print("Нечетное")

#next_task
num = int(input())
first_digit = num // 1000
second_digit = num // 100 % 10
third_digit = num % 100 // 10
fourth_digit = num % 10
if first_digit + fourth_digit == second_digit - third_digit:
    print("ДА")
else:
    print("НЕТ")

#next_task
age = int(input())
if age < 18:
    print("Доступ запрещен")
else:
    print("Доступ разрешен")

#next_task
num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

if num_2 - num_1 == num_3 - num_2:
    print("YES")
else:
    print("NO")

#next_task
first_entered_number = int(input())
second_entered_number = int(input())
if first_entered_number < second_entered_number:
    print(first_entered_number)
else:
    print(second_entered_number)

#next_task
first = int(input())
second = int(input())
third = int(input())
fourth = int(input())
print(min(first, second, third, fourth))

#next_task
years_old = int(input())
if years_old <= 13:
    print("детство")
elif years_old <= 24 >= 14:
    print("молодость")
elif years_old <= 59 >= 25:
    print("зрелость")
else:
    print("старость")

#next_task
ent_a = int(input())
ent_b = int(input())
ent_c = int(input())
counter = 0

if ent_a > 0:
    counter += ent_a
if ent_b > 0:
    counter += ent_b
if ent_c > 0:
    counter += ent_c
print(counter)