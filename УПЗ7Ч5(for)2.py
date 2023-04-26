x = "abcdefghijklmnopqrstuvwxyz"
y = input("Enter a string: \n")

for i in x:
    count = 0
    for r in y:
        if i == r:
            count +=1
    if count > 0:
        print("Letters", i, "were", count)

#next

for xx in range(2, 10, 2): #there are three parameters in 'range': start, stop, step.
    print(xx)

for xx in range(10, -10, -2):
    print(xx)