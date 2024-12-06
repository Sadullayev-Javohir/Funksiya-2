"""Arifmetik amallami bajaruvchi Calc (A, B, Op) funksiyasini hosil qiling.
A va B haqiqiy sonlar. Op o'zgaruchisi orqali bajariladigan arifmetik 
amal aniqlanadi. 1 - ayirish, 2-ko'paytirish, 3- bo'lish, boshqalari
qo'shish. Shu funksiya orqali A va B sonlari uchun N1, N2, N3, N4 
amallari bajarilsin. (N1-N4 butun sonlar)"""

def Calc(A, B, Operator):
    if Operator == 1:
        return f"{A} - {B} = {A - B}"
    elif Operator == 2:
        return f"{A} * {B} = {A * B}"
    elif Operator == 3:
        return f"{A} / {B} = {A / B}"
    elif Operator == 4:
        return f"{A} + {B} = {A + B}"

N1 = int(input("N1: "))
N2 = int(input("N2: "))

Operator = int(input("1-4: "))

print(Calc(N1, N2, Operator))