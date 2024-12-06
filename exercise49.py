"""EKUB funksiyasidan foydalangan holda (FunSimple46 masalasiga
 qarang) butun qiymat qaytaruvchi EKUB3(A, B, C) funksiya sini 
 hosil qiling. Funksiya A, B, C sonlarining eng kichik umumiy
 karralisini qaytarsin. A, B, C, D sonlari berilgan. (A, B, C).
(A, C, D), (A, B, D) sonlari uchun EKUB hisoblansin."""

def EKUB2(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def EKUB3(a, b, c):
    return EKUB2(EKUB2(a, b), c)

A = int(input("A sonni kiriting: "))
B = int(input("B sonni kiriting: "))
C = int(input("C sonni kiriting: "))
D = int(input("D sonni kiriting: "))

print(A, B, C)
print(A, C, D)
print(A, B, D)