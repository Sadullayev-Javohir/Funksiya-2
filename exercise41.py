"""Haqiqiy qiymat qaytaruvchi sin1(x, n) funksiyasini hosil qiling.
(x- haqiqiy son, n > 0) Funksiya quyidagi yig'indi qiymatini qaytarsin.
Sin(x)=x-x/(3!) + x/(5!) - ... +(-1)**n * x**(2n+1) / (2*n+1)! ) + ..."""
import math

def sin1(x, n):

    total = 0

    for k in range(n+1):
        total += (-1) ** k * (x ** (2 * k + 1)) / math.factorial(2 * k + 1)
        
    return total

X = int(input("X sonni kiriting: "))
N = int(input("N - darajani kiriting: "))

print(sin1(X, N))