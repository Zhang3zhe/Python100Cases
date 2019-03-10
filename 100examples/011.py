# Script based python 3.7

def rabbitNumber(month):
    list = [1,0,0,0]
    for i in range(month):
        x = list[0]
        y = list[1]
        z = list[2]
        w = list[3]
        list[0] = z + w
        list[1] = x
        list[2] = y
        list[3] = z + w
    return list[0] + list[1] + list[2] + list[3]

month = int(input('Please input month:'))
print(rabbitNumber(month))
