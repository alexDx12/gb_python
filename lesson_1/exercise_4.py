user_number = input("Введите целое положительное число: ")
i = 0
max_user_number = int(user_number[0])
while i < len(user_number):
    number = int(user_number[i])
    if number > max_user_number:
        max_user_number = number
    i += 1
print(f"Самая большая цифра в числе: {max_user_number}")

# вопрос: чем и когда лучше комментирвать блоки кода - кавычками или апострофами?

# вопрос: ниже код не работет корректно, это из-за того, что нельзя совмещать операцию сравнения if и операцию преобразования int?
'''while i < len(user_number):
    if int(user_number[i]) > max_user_number:
        max_user_number = user_number[i]
    i += 1
print(max_user_number)'''
