#topic: conditional statements in python

x = 0
if x == 0:
    print("if")
elif x > 0:
    print("elif")
else:
    print("else")

if x == 0:
    x +=1
print(x)

#2part

x = 5

if x == 0:
    x = 1
    print("x was zero")
elif type(x) == int or type(x) == float:
    print("x is OK")
else:
    print("x is wrong type")
    x = 1
print(100/x)

if not 1 == 0 and not 1 == 2:
    print("1 != 0")

