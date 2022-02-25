#!/usr/bin/python

from math import ceil,sqrt
import numpy as np
#from memory_profiler import profile
import ipdb

@profile
def gen_primes(n):
    l = range(2,n)
    primes = []
    for j in range(0,len(l)):
        p = True
        for d in primes:
            if(d > sqrt(l[j])):
                break
            if(l[j] % d == 0):
                p = False
                break;
        if(p):
            primes.append(l[j])

    return primes

@profile
def factorize(n,primes): ### High increment in memory usage
                         ### these lines would be good to optimise 
    ipdb.set_trace()
    factors = [None] * 20 ### Faster to create a vector beforehand
                          ### instead of appending in a loop
    dummy = 0
    init_n = n
    for p in primes:
        while(n%p == 0):
            n = n/p
            factors[dummy] = p
            dummy += 1
        if(p*p > n): # sqrt is slow
            break
    if(n > 1):
        factors[dummy] = n
    return factors[:dummy]

def phi(n,primes):
    factors = factorize(n,primes)
    p = 1

    for i in range(2,n):
        flag = True
        for f in factors:
            if i%f == 0:
                flag = False
                break
        if flag:
            p+=1
    return p

### This segment takes the longest time
@profile
def fast_phi(n,primes):
    factors = factorize(n,primes)### High increment in memory usage
    phi = factors[0]-1

    for i in range(1,len(factors)):
        if(factors[i] == factors[i-1]):
            phi *= factors[i]-1*(factors[i])/factors[i]-1
        else:
            phi *= factors[i]-1
    return phi

primes = gen_primes(1000)### Returns a list
m = 10000
#m = 8
fraq = 0
for i in range(2,m+1):
    fraq += fast_phi(i,primes)

print(fraq)
