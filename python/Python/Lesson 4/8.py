# Baranova Anastasia, RUDN, НБИбд-01-21, 08.05.22
# N 11.36

a = [2, 4, 8, 16, 32, 64, 128, -256, -512, -1024]
print("неотрицательные элементы:")
for i in range(10):
    if a[i] >= 0:
        print(a[i])
print("элементы, не превышающие число 100:")
for i in range(10):
    if a[i] <= 100:
        print(a[i])