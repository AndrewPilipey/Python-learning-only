x = 0b11110 #binary number system (двоичная). Пишем 0b и далее в двоичной
print("Вывод из двоичной в десятичную (это по умолчанию):", x)
print("Вывод из двоичной в двоичной:", bin(x))

y = 0o73021 #octal number system (восьмеричная). Пишем 0o и далее в восьмеричной.
print("Вывод из восьмеричной в десятичную (это по умолчанию):", y)
print("Вывод из восьмеричной в восьмеричной:", oct(y))

z = 0x77aa #hexadecimal number system (шестнадцатиричная). Пишем 0x и далее в шестнадцатиричной.
print("Вывод из шестнадцатеричной в десятичную (это по умолчанию):", z)
print("Вывод из шестнадцатеричной в шестнадцатеричную:", hex(z))

#PYTHON умеет воспринимать вплоть до 36-ричной системы счисления. Т.е. от 0 до 9 и от A до Z. Например:
s = int("Z3F", base=36)
print(int(s))

w = int(input(), base=8)
print(oct(w))

########################################
# Алгоритм получения цифр n-значного числа
# Несложно понять, по какому алгоритму можно найти каждую цифру n-значного числа num:
#
# Последняя цифра: (num % 101) // 100;
# Предпоследняя цифра: (num % 102) // 101;
# Предпредпоследняя цифра: (num % 103) // 102;
# .....
# Вторая цифра: (num % 10n-1) // 10n-2;
# Первая цифра: (num % 10n) // 10n-1.
########################################

