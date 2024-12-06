"""Haqiqiy qiymat qaytaruvchi RadToDeg (R) funksiyasini hosil 
qiling. Funksiya R radianning gradus qiymatini qaytarsin. Shu 
funksiya orqali radianda berilgan 3 ta burchakning gradusdagi 
qiymati aniqlansin."""

R = int(input("D sonni kiriting: "))

def RadtoDeg(R):
    pi = 3.14
    if 0 < R:
        Gradus = (R * 180) / pi
        return Gradus
    
print(RadtoDeg(R))