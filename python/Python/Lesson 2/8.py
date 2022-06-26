# Baranova Anastasia, RUDN, НБИбд-01-21, 26.03.22
# Задание 4, N1

import math

x = float(input())
y = float(input())
if math.fabs(x) + math.fabs(y) >= 1 and math.fabs(x) + math.fabs(y) <= 2:
    print("Yes")
else:
    print("No")