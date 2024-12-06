"""Haqiqiy qiymat qaytaruvchi Power3(A, N) funksiyasini hosil 
qiling. Funksiyada AN darajasi qiymati quyidagicha topilsin. 
Agar N sonining kasr qismi 0 dan farqli bo'lsa, Power2(A, N) 
funksiyasi chaqirilsin. Aks holda Power1(A, B) funksiyasi 
chaqirilsin (FunSimple37, FunSimple 38 masalalarga qarang). 
Shu funksiya orqali berilgan A sonining N, M, K darajalari 
topilsin. A, N, M, K haqiqiy sonlar. Eslatma: Power2(A, N) - 
funksiyasini chaqirishda N-sonining butun qismi jo'natiladi."""

def Power(A, N):
    if N > 0:
        return A ** N
    elif 0 > N:
        return 1 / (A ** abs(N))
    elif N == 0:
        return 1

N = int(input("N - darajani kiriiting: "))
M = int(input("M - darajani kiriiting: "))
K = int(input("K - darajani kiriiting: "))
A = int(input("A ni kiriiting: "))

print(Power(A, N))
print(Power(A, M))
print(Power(A, K))