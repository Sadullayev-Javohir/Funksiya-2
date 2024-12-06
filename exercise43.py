"""Haqiqiy qiymat qaytaruvchi Ln1(x n) funksiyasini hosil qiling.
(x <1, n> 0) Funksiya quyidagi yig'indi qiymatini qaytarsin.
In(1+x)=x-x/2+x3/3 - ... +(-1)**n * x**(n+1)/(n+1)+..."""


import math

def Ln1(x, n):

    total = 0

    for k in range(n+1):
        total += ((-1) ** k) * ((x ** (k + 1)) / (k + 1))
        # result += (-1)**(n+1) * (x**n) / n
        
    return total

X = float(input("X sonni kiriting: "))
N = int(input("N - darajani kiriting: "))

print(Ln1(X, N))