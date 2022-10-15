def gap(g, m, n):
    # your code
    prime_pair=[] 
    primes=[]
    #Loop to find all prime numbers inclusive of the range
    for i in range(m,n+1):
        factor_count=0
        for j in range(1,i+1):
            if i%j==0:
                factor_count+=1
        if factor_count==2:
            primes.append(i)
    run=True
    for i in range(len(primes)):
        for j in primes:
            if primes[i]!=j and j-primes[i]==g:
                prime_pair.append(primes[i])
                prime_pair.append(j)
                run=False
                break
        if run==False:
            break    
            
            
    print(prime_pair)
gap(6,100,110)
        