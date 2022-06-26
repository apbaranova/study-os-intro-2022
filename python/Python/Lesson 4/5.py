# Baranova Anastasia, RUDN, НБИбд-01-21, 08.05.22
# N 9.90

print("Введите предложение:")
s = input()
for i in range(len(s)):
    if s[i] == "e":
        s1 = s[0:i]
        s2 = s[i+1:len(s)]
        s = s1 + "u" + s2
print(s)