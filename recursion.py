one = [1, 4, 6]
two = [1, 2, 6, 8]
m = len(one)
n = len(two)
sortedList = []
i1 = 0
i2 = 0

for i in range(m+n):
    if i1 == m:
        sortedList.append(two[i2])
        i2 += 1
        
    elif i2 == n:
        sortedList.append(one[i1])
        i1 += 1

    else:
        if one[i1] <= two[i2]:
            sortedList.append(one[i1])
            i1 += 1
        else:
            sortedList.append(two[i2])
            i2 += 1
    


array  = [1,2,3,4]
array.insert(3, 5)
print(array)
