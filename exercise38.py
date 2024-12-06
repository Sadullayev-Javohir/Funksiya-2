"""Haqiqiy qiymat qaytaruvchi Power2(A, N) funksiyasini hosil 
qiling. Funksiyada AN darajasi qiymati quyidagi formula asosida
topilsin. Shu funksiya orqali berilgan A sonining N, M, K darajalari
topilsin. A° = 1; Agar N >0 bo'lsa, AN = A* A* ... *A 
(N ta ko'payuvchi). Agar A < 0 bo'lsa, AN=1/(A*A*... *A) 
(N ta ko'payuvchi). A haqiqiy, N, M, K butun sonlar."""

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