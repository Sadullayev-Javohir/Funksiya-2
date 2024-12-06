""" X va Y butun sonlari berilgan (X va Y noldan farqli). (X, Y) nuqta 
qaysi chorakda ekanini aniqlovchi Quarter nomli funksiya hosil qiling. 
Bu funksiya orqali 4 ta nuqtaning choragini aniqlang."""

def Quarter(X, Y):
    if X > 0 and Y > 0:
        return "1-chorak"
    elif X < 0 and Y > 0:
        return "2-chorak"
    elif X < 0 and Y < 0:
        return "3-chorak"
    elif X > 0 and Y < 0:
        return "4-chorak"


X = int(input("X sonni kiriting: "))
Y = int(input("Y sonni kiriting: "))

print(Quarter(X, Y))