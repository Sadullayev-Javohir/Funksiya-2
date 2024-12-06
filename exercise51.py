"""IncTime (H, M, S, T) funksiyasini hosil qiling. Funksiya
berilgan H-soat, M - minut, S- sekundni, T sekundga oshirsin.
Funksiya orqali berilgan soat, minut va sekundni T sekundaga 
oshiruvchi programma tuzilsin."""

def IncTime(H, M, S, T):
    total = 0
    H *= 3600
    M *= 60
    S *= 1
    T = T
    total += H + M + S + T
    return total

print(IncTime())