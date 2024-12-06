"""Butun qiymat qaytaruvchi Fib(N) funksiyasini hosil qiling. 
(N>0). Funksiya Fibonachchi sonlarining N-elementini qaytarsin.
Funksiyaga oid qo'shimcha masalalar"""

N = int(input("N sonini kiriting: "))

def fibonacci(n):
    if n <= 1:
        return n
    else:  
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(N))