"""IsSquare(K) mantiqiy funksiyasini hosil qiling. (K > 0). Agar K biror
butun soming kvadrati bo'lsa - true, aks xolda false qiymat qaytarilsin.
Shu funksiya orqali 3 ta sonni tekshiring."""

def IsSquare(K):
    if K < 0:
        return "minus son"
    else:
        while K % 2 == 0:
            K //= 2
        return K == 1

print(IsSquare(-8))
print(IsSquare(4))
print(IsSquare(6))
print(IsSquare(12))
print(IsSquare(32))