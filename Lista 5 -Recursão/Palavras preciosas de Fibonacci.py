def fibonacci(num):
    if num == 0:
        return "Precious"
    if num == 1:
        return "My"
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

numero = int(input())
print(fibonacci(numero))