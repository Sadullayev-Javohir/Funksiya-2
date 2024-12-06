"""Mantiqiy qiymat qaytaruvchi IsLeap Year(Y) funksiyasini hosil
qiling. Funksiya berilgan Y -yil kabisa yili bo'lsa true, aks
holda false qiymat qaytarsin. Berilgan 5 ta yilning kabisaligi
tekshirilsin."""


def IsLeapYear(year):
    check = (year % 100 == 0)
    check1 = check % 400 == 0 and year % 4 == 0

    return (check1)

year = int(input("Yil kiriting: "))

print(IsLeapYear(year))