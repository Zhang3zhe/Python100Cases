# Script based python 3.7

date = input("Input a date:\n")
date_s = date.split(' ')
year = int(date_s[0])
month = int(date_s[1])
day = int(date_s[2])
x = [year,month,day]
x.sort()
print(x)
