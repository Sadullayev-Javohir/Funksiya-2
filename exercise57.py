"""Leng funksiyasidan foydalangan xolda, haqiqiy qiymat qaytaruvchi 
Perim(XA, YA, XB,YB, Xc, Yc) funksiyasini hosil qiling. Funksiya berilgan koordinatalar
asosida uchburchak perimatrini qaytarsin. A, B, C, D nuqtalar koordinatalari 
berilgan. ABC, ABD, ACD uchburchaklar perimetrlari hisoblansin. """

import math

def Leng(X1, Y1, X2, Y2):
    PQ = math.sqrt(((X2 - X1) ** 2) + ((Y2 - Y1) ** 2))

    return PQ

def Perim(Ax, Ay, Bx, By, Cx, Cy):
    AB = Leng(Ax, Ay, Bx, By)
    AC = Leng(Ax, Ay, Bx, By)
    BC = Leng(Ax, Ay, Cx, Cy)

    return AB + AC + BC

Ax, Ay = float(input("Ax ni kiriting: ")), float(input("Ay ni kiriting: "))
Bx, By = float(input("Bx ni kiriting: ")), float(input("By ni kiriting :"))
Cx, Cy = float(input("Cx ni kiriting: ")), float(input("Cy ni kiriting :"))
Dx, Dy = float(input("Dx ni kiriting: ")), float(input("Dy ni kiriting :"))


PerimetrABC = Perim(Ax, Ay, Bx, By, Cx, Cy)
PerimetrABD = Perim(Ax, Ay, Bx, By, Dx, Dy)
PerimetrACD = Perim(Ax, Ay, Cx, Cy, Dx, Dy)


print(f"|ABC| = {PerimetrABC}\t |ABD| = {PerimetrABD}\t |ACD| = {PerimetrACD}")