print("*" * 15, "Calculator", "*" * 10)
print("To get out of here you can enter 'q' as the operation sign")
while True:
    s = input("Sign (+, -, *, /): ")
    if s == 'q': break
    if s in ('+', '-', '*', '/'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+':
            print("%.2f" % (x+y))
        elif s == '-':
            print("%.2f" % (x-y))
        elif s == '*':
            print("%.2f" % (x*y))
        elif s == '/':
            if y !=0:
                print("%.2f" % (x/y))
            else:
                print("divided by zero is impossible")
    else:
        print("Wrong sign of operation")
