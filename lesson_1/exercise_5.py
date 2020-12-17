gain = float(input("Введите сумму выручки, у.е.: "))
costs = float(input("Введите сумму издержек, у.е.: "))
if gain > costs:
    print("Фирма получила прибыль.")
    profitability = gain / costs
    print(f"Рентабельность фирмы составила: {profitability}")
    human_resource = float(input("Введите численность персонала, ед: "))
    specific_profitability = profitability / human_resource
    print(f"Прибыль фирмы в расчёте на одного сотрудника, у.е.: {specific_profitability}")
elif gain == costs:
    print("Фирма достигла точки безубыточности.")
else:
    print("Фирма получила убыток.")
