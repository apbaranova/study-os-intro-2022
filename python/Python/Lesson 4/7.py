# Baranova Anastasia, RUDN, НБИбд-01-21, 08.05.22
# N 11.16

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("а) Введите s:")
s = int(input())
if a[s] > 0:
    print(s,"элемент является положительным")
else:
    print(s,"элемент не является положительным")
print("б) Введите k:")
k = int(input())
if a[k] % 2 == 0:
    print(s,"элемент является четным числом")
else:
    print(k,"элемент не является четным числом")
print("в) ")
if a[k] > a[s]:
    print(k,"элемент больше",s,"элемента")
elif a[s] > a[k]:
    print(s,"элемент больше",k,"элемента")