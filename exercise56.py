"""Haqiqiy qiymat qaytaruvchi Leng(X1, Y1, X2, Y2) funksiyasini hosil qiling. Funksiya
berilgan (X1, Y1) va (X2, Y2) nuqtalar orasidagi masofani qaytarsin. A, B, C, D 
nuqtalar koordinatalari berilgan. A nuqtadan B, C, D nuqtalargacha bo'lgan masofa 
lar hisoblansin. |AB|, |AC|, |AD| - ?"""

import math

def Leng(X1, Y1, X2, Y2):
    PQ = math.sqrt(((X2 - X1) ** 2) + ((Y2 - Y1) ** 2))

    return PQ

Ax, Ay = float(input("Ax ni kiriting: ")), float(input("Ay ni kiriting: "))
Bx, By = float(input("Bx ni kiriting: ")), float(input("By ni kiriting :"))
Cx, Cy = float(input("Cx ni kiriting: ")), float(input("Cy ni kiriting :"))
Dx, Dy = float(input("Dx ni kiriting: ")), float(input("Dy ni kiriting :"))


AB = Leng(Ax, Ay, Bx, By)
AC = Leng(Ax, Ay, Cx, Cy)
AD = Leng(Ax, Ay, Dx, Dy)

print(f"|AB| = {AB}\t |AC| = {AC}\t |AD| = {AD}")