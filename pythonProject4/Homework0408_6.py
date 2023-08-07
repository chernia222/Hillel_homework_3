#Написати функцыю, яка буде рекурсивно вираховувати число фібоначчі.
#Число фібоначчі - це число, яке дорівнює суммі двох попередніх в
# послідовності (це і повинно бути в рекурсії). Закінчується на двох одиницях
def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

num = 6
result = fibonacci_recursive(num)
print(f"Число Фібоначчі для n = {num}: {result}")
