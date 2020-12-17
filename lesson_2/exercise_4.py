list = []
string = input("Введите строку из слов через пробел: ")
word_list = string.split()
n = 1
for word in word_list:
    if len(word) > 10:
        word = word[:10] + "..."
    print(f"{n}: {word}")
    n += 1