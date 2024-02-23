one = [1, 4, 6, 9]
two = [1, 2, 6, 8]

sortedList = []
i1 = 0
i2 = 0

def mergeSorted(listOne, listTwo):
    if len(listOne) < i1 and len(listTwo) < i2:
        return
    
    if listOne[i1] < listTwo[i2]:
        sortedList.append(listOne[i1])
        i1 += 1
        print(i1)
    else:
        sortedList.append(listTwo[i2])
        i2 += 1
        print(i2)


mergeSorted(one, two)
