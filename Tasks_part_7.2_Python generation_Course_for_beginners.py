#task
m, n = int(input()), int(input())
for i in range(m, n + 1):
    print(i)

#next_task
m_1, n_1 = int(input()), int(input())
if m_1 < n_1:
    for i in range(m_1, n_1 + 1):
        print(i)
else:
    for i in  range(m_1, n_1 - 1, - 1):
        print(i)

#next_task
m_2, n_2 = int(input()), int(input())
for i in range(m_2, n_2 - 1, -1):
    if i % 10 % 2 != 0:
        print(i)


#next_task
m_3, n_3 = int(input()), int(input())
for i in range(m_3, n_3 + 1, 1):
    if i % 17 == 0 or i % 10 == 9 or i % 3 == 0 and i % 5 == 0:
        print(i)

#next_task
times_m = int(input())
for i in range(1, 11, 1):
    print(times_m, "x", i, "=", times_m * i)






