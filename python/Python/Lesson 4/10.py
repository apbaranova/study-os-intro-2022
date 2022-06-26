# Baranova Anastasia, RUDN, НБИбд-01-21, 08.05.22
# N 11.108

from random import randrange
j = [randrange(100,1000) for i in range(100)]
print(j)
number = 0
for i in range (100):
    if j[i] > number:
        number = j[i]
print ("количество страниц в самой толстой книге:",number)