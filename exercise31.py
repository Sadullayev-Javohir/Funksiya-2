"""IsPalindrom(N) mantiqiy funksiya sini hosil qiling. (N > 0).
 Agar N soni palindrom bo'lsa - true, aks holda false qiymat 
 qaytarilsin. Shu funksiya orqali 5 ta sondan nechtasi palindrom
ekanini aniqlovchi programma tuzilsin. IsPalindrom 
funksiyasinida DigitCount va DigitN funksiyalridan foydalanish
mumkin. (Qarang FunSimple29, FunSimple 30)"""

N = int(input("N sonini kiriting: "))
N = str(N)
reverse = N[::-1]

def IsPalindrom(N):
    return N == reverse

print(IsPalindrom(N))



