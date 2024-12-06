""" Butun qiymat qaytaruvchi DigitCount(K) funksiyasini hosil qiling. 
(K> 0). Funksiya K ning raqamlari sonini qaytarsin. Shu funksiya orqali 5 ta
sonning raqamlari soni aniqlansin"""

K = int(input("K sonini kiriting :"))

def DigitCount(K):
    K = str(K)
    length = 0
    for i in K:
        if i in "-":
            length += 1
            lengthM = length - 1
            length =lengthM
        else:
            length += 1
    return length

print(DigitCount(K))