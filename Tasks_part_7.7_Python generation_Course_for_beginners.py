#________________CODE  REVIEW________________

# count = 0
# p = 1 #3 done
# for i in range(1, 11): #1 done
#     x = int(input())
#     if x >= 0: #4 done
#         p = p * x
#         count = count + 1
# if count > 0:
#     print(count) #2done
#     print(p)
# else:
#     print('NO')


#next_code_review

# mx = -999999999999
# s = 0
# for i in range(10):
#     x = int(input())
#     if x < 0:
#         s += x
#         if 0 > x > mx:
#             mx = x
# if s >= 0:
#     print("NO")
# elif s < 0:
#     print(s)
#     print(mx)


#next_code_review

# s = 0 #1 done
# for _ in range(1, 8): #2 done
#     n = int(input()) #3 done
#     if n % 2 == 0: #4 done
#         s = s + n
# print(s)


#next_code_review

n = int(input())
max_digit = -1 #3 done

while n > 0:
    digit = n % 10
    if digit % 3 == 0:

        if digit > max_digit: #1 done
            max_digit = digit #4 done

    n = n // 10 #2 done
if max_digit == -1: #5 done
    print('NO')
else:
    print(max_digit)


#next_code_review

n = int(input())
while n > 9:
    n //= 10
print(n)
