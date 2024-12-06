"""Haqiqiy qiymat qaytaruvchi Arctg1 (x, n) funksiyasini hosil 
qiling. (x < 1, > 0) Funksiya quyidagi yig'indi qiymatini 
qaytarsin.
arctg(x)=x-x3/3+x5/5-... +(-1)**n * x**(2*n+1) / (2n+ 1) + ..."""


import math

def Arctg1(x, n):

    total = 0

    for k in range(n+1):
        total += ((-1) ** k) * ((x ** (2 * k + 1)) / (2 * k + 1))
        
    return total

X = float(input("X sonni kiriting: "))
N = int(input("N - darajani kiriting: "))

print(Arctg1(X, N))