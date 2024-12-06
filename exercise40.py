"""Haqiqiy qiymat qaytaruvchi Exp1(x, n) funksiyasini hosil 
qiling. (x - haqiqiy son, &> 0) Funksiya quyidagi yig'indi qiymatini
qaytarsin. 1+x+x**2/(2!)+x**3 /(3!) + ... +x**n /(n!) +"""

import math

def Exp1(x, n):
    total = 0
    for k in range(n+1):
        total += (x ** k) / math.factorial(k)
    return total
X = int(input('X sonni kiriting: '))
N = int(input('N - darajani kiriting: '))

print(Exp1(X, N))