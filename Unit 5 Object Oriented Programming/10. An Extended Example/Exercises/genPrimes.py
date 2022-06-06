def genPrimes():
    primes = [2]
    count = 3
    count2 = 0
    while True:
        for element in primes:
            if count % element != 0:
                count2 += 1
        if count2 == len(primes):
            primes.append(count)
            yield primes[-2]
        count += 1
        count2 = 0

Pri = genPrimes()
print(Pri.__next__())
print(Pri.__next__())
print(Pri.__next__())
print(Pri.__next__())
