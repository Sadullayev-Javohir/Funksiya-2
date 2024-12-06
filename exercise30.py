"""Butun qiymat qaytaruvchi DigitN(K, N) funksiyasini hosil qiling.
(K > 0). Funksiya K sonining N- raqamini qaytarsin. Agar K soni
raqamlari N dan kichk bo'lsa, minus bir qaytarilsin. Shu funksiya
orqali K1, K2, K3 sonlarining N- raqami aniqlansin"""

K = int(input("K sonini kiriting: "))
N = int(input("N sonini kiriting: "))


def DigitN(K, N):
    if K < N:
        return  -1
    
    K = str(K)
    K = list(K)
    N = str(N)

    for i in K:
        if i == N: 
            return i
        
print(DigitN(K, N))