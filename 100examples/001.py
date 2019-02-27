list = [1,2,3,4]
count = 0
for i in list:
    for j in list:
        for k in list:
            if i!=j and i!=k and j!=k:
                print(i,j,k)
                count += 1
print(count)
