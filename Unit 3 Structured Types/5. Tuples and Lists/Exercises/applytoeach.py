def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

testList = [1, -4, 8, -9]
applyToEach(testList, abs)
print(testList)


def applyToEachV2(a):
    return a + 1

testList1 = [1, -4, 8, -9]
applyToEach(testList1, applyToEachV2)
print(testList1)


def applyToEachV3(a):
    return a**2

testList2 = [1, -4, 8, -9]
applyToEach(testList2, applyToEachV3)
print(testList2)
