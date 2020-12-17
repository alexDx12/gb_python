
# data = [(1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
#         (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
#         (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})

index = 1
result = []
spec = ["название", "цена", "количество", "ед"]

while True:
    question = input("Добавить новый товар да/нет? ")
    if question.upper() == "НЕТ":
        break

    item = {}

    for spe in spec:
        user_data = input(f"Введите {spe}: ")
        if user_data.isdigit():  # isdigit проверяет является ли переменная целым числом
            item[spe] = int(user_data)
        else:
            item[spe] = user_data

    result.append(tuple[index, item])
    index += 1

res_dict = {}

for item in spec:
    for param in result:
        if res_dict.get(item):
            res_dict[item].append(param[1].get(item))
        else:
            res_dict[item] = [param[1].get(item)]

print(res_dict)

# помогите пожалуйста разобраться, при выполнении кода получаю ошибку: TypeError: There are no
# type variables left in tuple...