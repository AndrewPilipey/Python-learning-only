#task
n = int(input())
while n != 0:
    last_digit = n % 10
    print(last_digit)
    n = n // 10

#nextTask
startNum = int(input())
reverseNum = ""
while startNum != 0:
    reverseNum += str(startNum % 10)
    startNum = startNum // 10
reverseNum = int(reverseNum)
print(reverseNum)

#nextTask
enteredNum = int(input())
maxNum = 0
minNum = 9
while enteredNum != 0:
    lastDigit = enteredNum % 10
    if lastDigit > maxNum:
        maxNum = lastDigit
    if lastDigit < minNum:
        minNum = lastDigit
    enteredNum = enteredNum // 10
print("Максимальная цифра равна", maxNum)
print("Минимальная цифра равна", minNum)

#nextTask
a = int(input())
sum_a = 0
quantity_of_digits_a = 0
product_of_digits = 1
average_a = 0
first_digit_a = 0
sum_first_last_digits = a % 10
while a != 0:
    last_digit = a % 10
    sum_a += last_digit
    quantity_of_digits_a += 1
    product_of_digits *= last_digit
    average_a += last_digit
    first_digit_a = last_digit
    a = a // 10
print(sum_a)
print(quantity_of_digits_a)
print(product_of_digits)
print(average_a / quantity_of_digits_a)
print(first_digit_a)
print(sum_first_last_digits + first_digit_a)

#nextTask
b = int(input())
second_digit = 0
quantity_of_digits_b = len(str(b))


if quantity_of_digits_b > 2:
    while b // 100 != 0:
        last_digit = b % 10
        b = b // 10
        second_digit = b
    print(second_digit % 10)
elif quantity_of_digits_b <= 3:
    print(b % 10)

#BUT IT'S MORE GREAT:
b = int(input())
while b > 99:
    b = b // 10
print(b % 10)

#nextTask
c = int(input())
flag = True
the_same = c % 10
while c != 0:
    last_digit = c % 10
    if the_same != last_digit:
        flag = False
        print("NO")
        break
    c = c // 10

if flag:
    print("YES")

#nextTask
d = int(input())
last_digit = d % 10
loc_flag = True
while d > 0:
    cur_digit = d % 10
    if last_digit > cur_digit:
        loc_flag = False
        print("NO")
        break
    last_digit = cur_digit
    d = d // 10
if loc_flag:
    print("YES")
