"""Haqiqiy qiymat qaytaruvchi cos1(x, n) funksiyasini hosil 
qiling. (x - haqiqiy son, ε > 0) Funksiya quyidagi yig'indi 
qiymatini qaytarsin. cos(x)=1-x2/(2!)+/(4!)... 
+(-1)**n / x(**2*n) /((2*n)!) +"""

import math

def cos1(x, n):

    total = 0

    for k in range(n+1):
        total += (-1) ** k / (x ** (2 * k)) / math.factorial(2 * k)
        
    return total

X = int(input("X sonni kiriting: "))
N = int(input("N - darajani kiriting: "))

print(cos1(X, N))