m = "string of text"
count = 0

for i in m:
    if i == 't':
        print('There is a letter "t" in the string')
        count += 1

else:
    print("cycle complete. Letters 't':", count)
print("The program continues")