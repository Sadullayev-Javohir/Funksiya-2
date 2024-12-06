"""Butun sonning juft-toqligini aniqlovchi Even(K) funksiyasini hosil 
qiling. Funksiya K juft son bo'lsa - true, aks xolda false qiymat 
qaytarsin. Bu funksiya orqali 3 ta sonning juft yoki toqligi aniqlansin."""

def Even(K):
    if K % 2 == 0 and K != 0:
        return "Juft"
    elif K % 2 == 1 and K != 0:
        return "Toq"
    
print(Even(0))