# n = list(range(10))
# m = []
# for i in n:
#     if i == 8:
#         continue
#     m.append(i)
# else:
#     print(m)

# x = [9, 8, 7, 6, 5]
# x.append(4) #метод append добавляет элемент в конец списка
# print(x)
# x.insert(6, 3) #метод insert добавляет элемент по указанному индексу (индекс, значение)
# print(x)
# print(x.count(9)) #count - указывает количество одинаковых элементов в списке.
# x.sort() #sort - сортирует элементы списка по возрастанию.
# print(x)
# x.reverse() #reverse -переворачивает список
# print(x)
# x.pop() #pop - удаляет элемент по индексу (если ничего не указать, то удалит последний элемент).
# print(x)
# y = x.pop() #pop может удалить элемент и мы можем сохранить его в переменную
# print(x, y, "pop")
# x.remove(5) #remove удаляет конкретный элемент (НЕ ПО ИНДЕКСУ)
# print(x, "remove")
# x.clear() #очищает список
# print(x, "clear")
# x.extend(['a']) #добавляет в конец списка элемент из другого списка
# print(x, "extend")
# h = x.copy()
# print(h, "this is 'h'")

n = list(range(1, 21))
b = n.copy() #/либо можно скопировать срезом b = n[::]
m = []
for i in n:
    if i % 2 == 0:
        m.append(i)
        n.remove(i)
else:
    print(n)
    print(m)
    print(b)

my_collection= list(range(1, 15))
print(my_collection)
my_collection_slice = my_collection[0:14:1] #[START:STOP:STEP]
print(my_collection_slice) #This is sintax of slices