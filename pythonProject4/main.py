#1 Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є буква "о"
# (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "о".
# while True:
#     word = input("Введіть слово: ")
#     if 'о' in word.lower():
#         break
#     else:
#         print("У слові відсутня буква 'о'")
# while True:
#     word = input("input word: ")
#     if 'o' in word.lower():
#         break
#     else:
#         print("'o' doesn't exist")
#2 Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який свормує новий list (наприклад lst2),
# який містить лише змінні типу стрінг, які присутні в lst1. Данні в лісті можуть бути будь якими

# lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
#
# lst2 = [x for x in lst1 if isinstance(x, str)]
#
# print(lst2)

#3 Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum_of_even_numbers = 0
for num in numbers:
    if num % 2 == 0:

        sum_of_even_numbers += num

print("sum of paire numbers:", sum_of_even_numbers)