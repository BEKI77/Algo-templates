def segmentedSieveNoPreGen(l,r)-> list:
    isPrime = [True for _ in range(r-l+1)]
    lim = int(r**(0.5))
    for i in range(2,lim+1):
        for j in range(max(i * i, (l + i - 1) / i * i), r+1, i):
            isPrime[j-l] = False
    if l==1:
        isPrime[0]=False
    
    return isPrime
