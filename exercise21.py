"""A va B sonlari orasidagi sonlar yig'indisini hisoblovchi SumRange (A, B)
nomli funksiya hosil qiling. Agar A > B bo'lsa, funksiya 0 qiymat 
qaytaradi. Bu funksiya orqali A dan B gacha va B dan C gacha bo'lgan 
sonlar yig'inddisini hisoblang. A, B, C butun sonlar."""



def SumRange(A, B):
    add = 1

    if A > B:
        return 0
    else:
        while A < B:
            A += 1
            add += A

    return(add)

A = int(input("A sonni kiriting: "))
B = int(input("B sonni kiriting: "))
C = int(input("C sonni kiriting: "))

print(SumRange(A, B))
print(SumRange(B, C))
