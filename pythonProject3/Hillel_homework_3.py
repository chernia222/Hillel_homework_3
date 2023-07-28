#Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()
#Домашне завдання_3
first_num = input("Enter name ")
unique_characters = set(first_num)
num_unique_characters = len(unique_characters)
second_num = 10

if num_unique_characters > second_num:
    print(True)
else:
    print(False)