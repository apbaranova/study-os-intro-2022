# Baranova Anastasia, RUDN, НБИбд-01-21, 26.03.22
# Задание 2, If10

A = int(input())
B = int(input())
if A != B:
    sum = A + B
    A = sum
    B = sum
else:
    A = 0
    B = 0
print("A =" , A)
print("B =" , B)