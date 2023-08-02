#Напишіть функцію, яка приймає два аргументи.
# Якщо обидва аргумени відносяться до числових типів функція пермножує
# ці аргументи і повертає результат
# Якшо обидва аргументи відносяться до типу стрінг функція обʼєднує їх в
# один і повертає
# В будь-якому іншому випадку - функція повертає кортеж з двох агрументів
# Імпортуйте цю функцію, і викличте в іншому файлі
from Homework0108_5 import process_arguments

result1 = process_arguments(16.2, 7.3)
result2 = process_arguments("Vova, ", "Chernia")
result3 = process_arguments(12.2, "Kyiv")

print("Result 1", result1, type(result1))
print("Result 2", result2, type(result2))
print("Result 3", result3, type(result3))
