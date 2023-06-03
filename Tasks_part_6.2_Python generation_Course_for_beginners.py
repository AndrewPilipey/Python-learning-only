#Task
print('"Python is a great language!", said Fred. ' + '"I don\'t ever remember having this much fun before."')

#next_task
firstName = input()
lastName = input()
print(f"Hello {firstName} {lastName}! You just delved into Python") #f-строки не сохраняются в памяти!

#next_task
soccerTeam = input()
print("Футбольная команда " + soccerTeam + " имеет длину " + str(len(soccerTeam)) + " символов")

#next_task
city_1, city_2, city_3 = input(), input(), input()
length_1, length_2, length_3 = len(city_1), len(city_2), len(city_3)
minimum = min(length_1, length_2, length_3)
maximum = max(length_1, length_2, length_3)
if minimum == length_1:
    print(city_1)
elif minimum == length_2:
    print(city_2)
elif minimum == length_3:
    print(city_3)
if maximum == length_1:
    print(city_1)
elif maximum == length_2:
    print(city_2)
elif maximum == length_3:
    print(city_3)

#next_task
a, b, c = input(), input(), input()
a_len = len(a)
b_len = len(b)
c_len = len(c)
middle = a_len + b_len + c_len - (max(a_len, b_len, c_len) + min(a_len, b_len, c_len))
if (max(a_len, b_len, c_len) + min(a_len, b_len, c_len)) / 2 == middle:
    print("YES")
else:
    print("NO")

#next_task
blue = input()
if "синий" in blue:
    print("YES")
else:
    print("NO")

#next_task
weekend = input()
if "суббота" in weekend or "воскресенье" in weekend:
    print("YES")
else:
    print("NO")

#next_task
email = input()
if "@" in email and "." in email:
    print("YES")
else:
    print("NO")