""" Butun qiymat qaytaruvchi EKUB(A, B) funksiyasini hosil qiling.
funksiya A va B sonlarining eng katta umumiy bo'luvchisini 
qaytarsin. A, B, C, D sonlari berilgan. (A, B), (A, C), (A.D)
juftliklari uchun EKUB hisoblansin."""

def EKUB(a, b):
    while b != 0:
        a, b = b, a % b
    return a  


A = int(input("A sonni kiriting: "))
B = int(input("B sonni kiriting: "))
C = int(input("C sonni kiriting: "))
D = int(input("D sonni kiriting: "))

print(EKUB(A, B))
print(EKUB(A, C))
print(EKUB(A, D))