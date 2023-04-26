# n = list(range(10))
# m = []
# for i in n:
#     if i == 8:
#         continue
#     m += [i]
# else:
#     print(m)

x = [9, 8, 7, 6, 5]
x.append(4) #метод append добавляет элемент в конец списка
print(x)
x.insert(6, 3) #метод insert добавляцет элемент по указанному индексу (индекс, значение)
print(x)
print(x.count(9)) #count - указывает количество одинаковых элементов в списке.
x.sort() #sort - сортирует элементы списка по возрастанию.
print(x)
x.reverse() #reverse -переворачивает список
print(x)
x.pop() #pop - удаляет элемент по индексу (если ничего не указать, то удалит последний элемент).
print(x)
y = x.pop()
print(x, y)