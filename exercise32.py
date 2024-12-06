"""Haqiqiy qiymat qaytaruvchi DegToRad(D) funksiyasini hosil 
qiling. (360 > D > 0). Funksiya D gradusning radian qiymatini 
qaytarsin. Shu funksiya orqali 3 ta berilgan burchakning radianga
qiymati aniqlansin."""

D = int(input("D sonni kiriting: "))

def DegToRad(D):
    pi = 3.14
    if 0 < D <= 360:
        Radian = (D * pi) / 180
        return Radian
    
print(DegToRad(D))