# Script based python 3.7

def isLeapYear(y):
    if (y%4==0 and y%100!=0) or y%400==0:
        return True
    else:
        return False

Table = ((0, 31,28,31,30,31,30,31,31,30,31,30,31),(0, 31,29,31,30,31,30,31,31,30,31,30,31))

date = input("Input a date:\n")
date_s = date.split(' ')
year = int(date_s[0])
month = int(date_s[1])
day = int(date_s[2])
sum = 0
for i in range(month):
    sum += Table[isLeapYear(year)][i]
sum += day
print(sum)
