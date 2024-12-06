"""IsPower5(K) mantiqiy funksiyasini hosil qiling. (K> 0). Agar K soni 5
ning biror darajasi bo'lsa - true, aks xolda false qiymat qaytarilsin Shu
funksiya orqali 5 ta sondan nechtasi 5 ning darajasi ekanini aniqlovchi
programma tuzilsin."""

def IsPower5(K):
    if K <= 0:
        return False
    while K % 5 == 0:  # Agar son 5 ga bo'linaversa
        K = K // 5
    return K == 1  # Oxirida 1 qolganda true qaytaradi

print(IsPower5(125))
print(IsPower5(75))
print(IsPower5(625))
print(IsPower5(65))
print(IsPower5(12))
