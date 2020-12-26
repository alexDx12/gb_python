my_list = [7, 5, 3, 3, 2]
new_item = int(input("Введите новый элемент рейтинга: "))
if new_item > max(my_list):
    my_list.insert(0, new_item)
elif new_item < min(my_list):
    my_list.append(new_item)  # вопрос: можно ли вставить элемент в конец списка функцией insert? как указать
    # последний индекс?
else:
    index = my_list.index(new_item)
    count = my_list.count(new_item)
    my_list.insert(index + count, new_item)
print(my_list)