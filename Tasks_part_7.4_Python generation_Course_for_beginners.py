fus = input()

while fus != "КОНЕЦ":
    print(fus)
    fus = int(input())


#nextTask
fus2 = input()

while fus2 != "КОНЕЦ" and fus2 != "конец":
    print(fus2)
    fus2 = input()

#nextTask
totalWords = 0
inputedWord = input()
while inputedWord != "стоп" and inputedWord != "хватит" and inputedWord != "достаточно":
    totalWords += 1
    inputedWord = input()
print(totalWords)

#nextTask
a = int(input())
while a % 7 == 0:
    print(a)
    a = int(input())

#nextTask
totalNum = 0
num = int(input())
while num >= 0:
    totalNum += num
    num = int(input())
print(totalNum)

#nextTask
b = int(input())
totalScore = 0
while 5 >= b >= 0:
    if b == 5:
        totalScore += 1
    b = int(input())
print(totalScore)

#nextTask
n = int(input())
counter = 0
while n >= 25:
    counter += 1
    n = n - 25
while n >= 10:
    counter += 1
    n = n - 10
while n >= 5:
    counter += 1
    n = n - 5
while n >= 1:
    counter += 1
    n = n - 1
print(counter)
