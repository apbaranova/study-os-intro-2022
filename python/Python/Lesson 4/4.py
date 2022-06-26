# Baranova Anastasia, RUDN, НБИбд-01-21, 08.05.22
# N 9.78

print("Введите слово:")
s = input()
p = s
fi = 1
for i in range(len(s)):
    if s[i] != s[-1]:
        fi = 0
        break
if i == 1:
    print("Yes")
else:
    print("No")