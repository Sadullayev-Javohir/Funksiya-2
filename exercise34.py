"""Butun qiymat qaytaruvchi Fact(N) funksiyasini hosil qiling.
(N > 0). Funksiya N! qiymatini qaytarsin. Shu funksiya orqali 3
ta sonlarining faktoriali aniqlansin."""

N = int(input("Son kiriting: "))


def Fact(N):
    factorial = 1
    if N > 0:
        for i in range(1, N + 1):
            factorial *= (i)
    return(factorial)

print(Fact(N))