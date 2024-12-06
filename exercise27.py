"""IsPowerN(K, N) mantiqiy funksiyasini hosil qiling. (K > 0). Agar K soni
N soninig biror darajasi bo'lsa - true, aks xolda false qiymat qaytarilsin.
Shu funksiya orqali 5 ta sondan nechtasi N ning darajasi ekanini aniqlovchi programma tuzilsin."""

def isPowerN(K, N):

    while K % N == 0:
        K //= N
    return(K == 1)

K = int(input("K son: "))
N = int(input("N son: "))

print(isPowerN(K, N))