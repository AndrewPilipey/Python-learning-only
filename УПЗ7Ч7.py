#tuples (кортежи)

# x = (9, 8, 7, 6, 5, 4, 3)
# y = []
# for i in range(len(x)):
#     y.append(x[i] +3)
#
#
# #a, b, c = x
# r = 5
# u = 4
# print(r, u)
# r, u = (u, r)
# print(r, u)
# print(x[1:5])

# x1 = (1, 2, 3, 4, 5)
# print(x1)
# t = list(x1)
# t[0] = 10
# x1 = tuple(t)
# print(x1) #эта часть кода: есть кортеж (он неизменяем).
# Мы переводим кортеж в список. Меняем нужное нам значение по индексу.
#Далее обратно переводим список в кортеж. That's all


#методы кортежей
g = (9, 8, 7, 6, 5, 9, 4, 3, 123)
print(g.count(9), 'count') #считает кол-во совпадений в кортеже
print(g.index(9), 'index') #показывает индекс, но только первого элем-та, который встретится.

p = (1, 2, 3)
#хоть кортеж и неизменяемы тип данных, но к нему можно добавить ещё один кортеж
p += (4, 5, 6)
print(p)
