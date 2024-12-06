"""EKUB funksiyasidan foydalangan holda butun qiymat qaytaruvchi
EKUK(A, B) funksiya sini hosil qiling. Funksiya Ava B sonlarining
eng kichik umumiy karralisini qaytarsin. A, B, C, D sonlari 
berilgan. (A, B), (A, C), (A, D) juftliklari uchun EKUK hisoblansin.
EKUK = A*B/EKUB(A, B);"""

def EKUB(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def EKUK(a, b):
    return a * b / EKUB(a, b)

A = int(input("A sonni kiriting: "))
B = int(input("B sonni kiriting: "))
C = int(input("C sonni kiriting: "))
D = int(input("D sonni kiriting: "))

print(EKUK(A, B))
print(EKUK(A, C))
print(EKUK(A, D))