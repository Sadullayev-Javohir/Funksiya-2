"""TimeToHMS(T, H, M, S) funksiyasini hosil qiling. Funksiya
berilgan T sekundni H- soat, M- minut, S - sekundlarga ajratsin.
Funksiya orqali berilgan T1, T2, T3 sekundlar soat, minut va 
sekundlarga aylanritilsin.
Masalan: T =400
Natija: 00:06:40"""

def TimeToHMS(T):
    H = T // 3600
    M = (T % 3600) // 60
    S = T % 60

    return f"{H:02}:{M:02}:{S:02}"

T = int(input("Sekund kiriting: "))

print(TimeToHMS(T))