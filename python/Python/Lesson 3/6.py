# Baranova Anastasia, RUDN, НБИбд-01-21, 13.04.22
# Задание 2, For17

A = float(input())
N = int(input())
i = 0
sum = 0
while i <= N:
    sum += A**i
    i += 1
print (sum)