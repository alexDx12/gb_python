items = input("Введите список целых чисел через пробел: ")
items_list = items.split()
list = []
for i in items_list:
    list.append(int(i))
even_list = []
odd_list = []
for i in list:
    tmp = list.pop(list.index(i))
    odd_list.append(tmp)
even_list = list
result_list = []
for i in range(len(even_list)):
    result_list.append(even_list[i])
    result_list.append(odd_list[i])
if len(odd_list) > len(even_list):
    result_list.append(odd_list.pop(-1))
print(result_list)