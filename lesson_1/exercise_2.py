input_seconds = int(input("Введите время в секундах: "))
hours = input_seconds // 3600
minutes = (input_seconds - hours * 3600) // 60
seconds = input_seconds - hours * 3600 - minutes * 60
print(f"Время в формате чч:мм:сс: {hours}:{minutes}:{seconds}")
