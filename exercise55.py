"""MonthDays funksiyasidan foydalangan xolda, NextDate(D, M, Y) funksiyasini hosil
qiling. Funksiya berilgan sanadan keying sanani aniqlasin, D kun, Y-yil, M - oyini
qaytarsin. 3 ta Berilgan sana dan keying sana aniqlansin. (FunSimple 53 masalaga 
qarang.)"""

def IsLeapYear(Y):
    check = Y % 100 == 0
    check1 = Y % 4 == 0 and check % 400 == 0

    return check1

def MonthDays(M, Y):
    months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if M == 2 and IsLeapYear(Y):
        return 29
    return months[M]

def NextDate(D, M, Y):
    nextDateMonth = MonthDays(M, Y)

    if D < nextDateMonth:
        return D + 1, M, Y
    else:
        if M < 12:
            return 1, M + 1, Y
        else:
            return 1, 1, Y + 1


year = int(input("Yilni kiriting: "))
month1 = int(input("1-oyni kiriting: "))
month2 = int(input("2-oyni kiriting: "))
month3 = int(input("3-oyni kiriting: "))
date1 = int(input("1-sanani kiriting: "))
date2 = int(input("2-sanani kiriting: "))
date3 = int(input("3-sanani kiriting: "))

print(f"{NextDate(date1, month1, year)}")
print(f"{NextDate(date2, month2, year)}")
print(f"{NextDate(date3, month3, year)}")