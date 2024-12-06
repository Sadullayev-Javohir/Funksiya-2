"""Haqiqiy qiymat qaytaruvchi Power1(A, B) funksiyasini hosil 
qiling. Funksiya AB darajasi qiymatini qaytarsin. Shu funksiya 
orqali berilgan A1, A2, A3 sonlarining B darajasi topilsin. A, 
A1, A2, A3, B haqiqiy sonlar."""

def Power1(A, B):
    return A ** B

A1 = int(input("A1 sonini kiriting: "))
A2 = int(input("A2 sonini kiriting: "))
A3 = int(input("A3 sonini kiriting: "))
B = int(input("Darajani kiriting: "))

print(Power1(A1, B))
print(Power1(A2, B))
print(Power1(A3, B))