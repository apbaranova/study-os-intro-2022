# Baranova Anastasia, RUDN, НБИбд-01-21, 13.04.22
# Задание 2, While3

n = int(input())
k = int(input())
a = 0
while n >= k:
    n -= k
    a += 1
print("частное:" , a , "остаток:" , n)