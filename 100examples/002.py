# Script based python 3.7

data   = int(input('Input the money (w)\n'))

if data>0 and data<=10:
    bonus = data * 0.1
elif data>10 and data<=20:
    bonus = 10*0.1 + (data-10)*0.075
elif data > 20 and data <= 40:
    bonus = 10*0.1 + 10*0.075 + (data-20)*0.05
elif data > 40 and data <= 60:
    bonus = 10*0.1 + 10*0.75 + 20*0.05 + (data-40)*0.03
elif data>60 and data<=100:
    bonus = 10 * 0.1 + 10 * 0.75 + 20 * 0.05 + 20 * 0.03 + (data-60)*0.015
else:
    bonus = 10 * 0.1 + 10 * 0.75 + 20 * 0.05 + 20 * 0.03 + 40*0.015 + (data-100)*0.01

print(bonus)
