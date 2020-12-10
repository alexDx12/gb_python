initial_result = float(input("Введите начальный результат, км: "))
target_result = float(input("Введите целевой результат, км: "))
current_result = initial_result
day_number = 1
while current_result < target_result:
    print(f"{day_number}-й день: {current_result} км")
    current_result = current_result * 1.1
    day_number += 1
print(f"Результат будет достигнут на {day_number}-й день")
