# Baranova Anastasia, RUDN, НБИбд-01-21, 08.05.22
# N 11.54

a = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
sum = 0
for i in range(10):
    if a[i] <= 20:
        sum += a[i]
print("суммa элементов массива, значение которых не превышает 20:",sum)
sum = 0
b = int(input())
for i in range(10):
    if a[i] > b:
        sum += a[i]
print("суммa элементов массива, больших числа b:",sum)