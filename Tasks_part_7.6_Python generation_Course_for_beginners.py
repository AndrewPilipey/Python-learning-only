# n = int(input())
# n2 = 0
# divide = 2
# while n % divide != 0:
#     n2 = n % divide
#     if n2 == 0:
#         break
#     divide += 1
#
# print(divide)

#but more great:
# n_test = int(input())
#
# for i in range(2, n_test+1):
#     if n_test % i == 0:
#         print(i)
#         break


#nextTask
a = int(input())
for i in range(1, a+1):
    if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
        continue
    print(i)