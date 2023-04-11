def oddNumbers(l, r):
    # diff = r - l
    arrOdd = []

    for i in range(l, r+1):
        if i % 2 != 0:
            arrOdd.append(i)

    return arrOdd


print(oddNumbers(1, 7))
