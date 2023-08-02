#Напишіть функцію, яка приймає два аргументи.
# Якщо обидва аргумени відносяться до числових типів функція пермножує
# ці аргументи і повертає результат
# Якшо обидва аргументи відносяться до типу стрінг функція обʼєднує їх в
# один і повертає
# В будь-якому іншому випадку - функція повертає кортеж з двох агрументів
# Імпортуйте цю функцію, і викличте в іншому файлі
def process_arguments(arg1, arg2):
    if isinstance(arg1, (int, float)) and isinstance(arg2, (int, float)):
        return arg1 * arg2
    elif isinstance(arg1, str) and isinstance(arg2, str):
        return arg1 + arg2
    else:
        return arg1, arg2
