"""IsLeap Year(Y) funksiyasidan foydalangan xolda, butun qiymat qaytaruvchi
MonthDays(M, Y) funksiyasini hosil qiling. Funksiya berilgan Y-yilning M - oyi 
kunlar sonini qaytarsin. Berilgan yilning M1, M2, M3 oylarining kunlar soni topilsin.
(FunSimple52 masalaga qarang.)"""


def IsLeapYear(year):
    check = (year % 100 == 0)
    check1 = check % 400 == 0 and year % 4 == 0

    return (check1)

year = int(input("Yilni kiriting: "))
month1 = int(input("1-oyni kiriting: "))
month2 = int(input("2-oyni kiriting: "))
month3 = int(input("3-oyni kiriting: "))

def MonthDays(M, Y):
    months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if M == 2 and IsLeapYear(Y):
        return 29
    return months[M]

DaysMonth1 = MonthDays(month1, year)
DaysMonth2 = MonthDays(month2, year)
DaysMonth3 = MonthDays(month3, year)

print(DaysMonth1, year)
print(DaysMonth2, year)
print(DaysMonth3, year)