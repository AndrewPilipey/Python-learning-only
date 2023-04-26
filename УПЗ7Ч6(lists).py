#lists

m = [1, 2, 1, 3, 4] #indices 0, 1, 2, 3, 4
print(type(m))

print(m[0]) #получаем индекс по обычной нумерации (индексы нумеруются с нуля)
print(len(m))
print(m[-1]) #и в питон есть обратная нумерация с конца: -1 (последний элемент), -2 и т.д

super_m = [1, 2, 3, 'a', 'b', 'c', [], [11, 'aa']]
print(super_m, super_m[-1], super_m[-1][1])
super_m[0] = 999
print(super_m)
super_m[0] = super_m[0] + 2
print(super_m)

super_m[1], m[2] = m[2], m[1] #replace
print(super_m)

super_m = super_m + ["new"]
print(super_m)
print("end")

#next
#формирование списка

n = list(range(10))
n2 = []
for i in n:
    if i == 8:
        continue
    n2 += [i]
else:
    print(n2)