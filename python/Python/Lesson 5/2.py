# Baranova Anastasia, RUDN, НБИбд-01-21, 27.05.22
# N7

def poli(n):
    k = n
    l = 0
    while k > 0:
        l = l * 10
        l += k % 10
        k //= 10
    if n == l:
        return 1
    else:
        return 0

a = int(input())
b = int(input())
if poli(a) == 1 or poli(b) == 1:
    print("Yes")
else:
    print("No")