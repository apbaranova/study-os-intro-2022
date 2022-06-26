# Baranova Anastasia, RUDN, НБИбд-01-21, 27.05.22
# N 10.41

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input())
print(factorial(n))