# Baranova Anastasia, RUDN, НБИбд-01-21, 27.05.22
# 10.12

from random import randrange

def even(n):
    if n % 2 == 0:
        return 1
    else:
        return 0

a = [randrange(1,100) for i in range(13)]
b = [randrange(1,100) for i in range(13)]
print(a)
print(b)
evenc = 0
for i in range(13):
    if even(a[i]) == 1:
        evenc += 1
print(evenc)
primc = 0
for i in range(13):
    if even(b[i]) == 0:
        primc += 1
print(primc)