#while

x = 0

while x < 5:
    x += 1
    print(x)
else:
    print("end")

#nexttask
#while True:
#    f = int(input("Enter f: "))
#    count = 0
#    y = 1

#   while count < f:
#      count += 1
#     y *= count

#else:
#   print(y)

#nexttask

xx = ""

while len(xx) < 5:
    yy = input("Enter a letter: ")
    if yy == "o":
        continue
    if yy == "l":
        break
    xx += yy
else:
    print(xx)