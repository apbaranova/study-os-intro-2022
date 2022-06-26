# Baranova Anastasia, RUDN, НБИбд-01-21, 08.05.22
# N 11.144

from random import randrange

a = [randrange(1,1000) for i in range(13)]
print(a)
a[1], a[4] = a[4], a[1]
print(a)
m = int(input())
n = int(input())
m -= 1
n -= 1
a[m], a[n] = a[n], a[m]
print(a)
max = 0
maxin = 0
for i in range (13):
    if a[i] > max:
        max = a[i]
        maxin = i
a[2], a[maxin] = a[maxin], a[2]
print(a)
min = 999
minin = 0
for i in range (13):
    if a[i] <= min:
        min = a[i]
        minin = i
a[0], a[minin] = a[minin], a[0]
print(a)