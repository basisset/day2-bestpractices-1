# Program to multiply two matrices using nested loops
import random
#from memory_profiler import profile
import numpy as np
import ipdb

N = 250


### 38 MiB
@profile

# NxN matrix
# Nx(N+1) matrix
def makeXY(N):
    #ipdb.set_trace()
    X = np.random.randint(0,100,(N,N))
    Y = np.random.randint(0,100,(N,N+1))
    return X,Y

### 39 MiB
@profile
def storing_results(N):
    result = np.zeros((N,N+1))
    return result
    # iterate through rows of X

    ### This segment takes the most time at about 13.3487 s
    ### 41 MiB
    ### There is probably a smarter way to multiply X and Y
    ### and since these lines takes the longest then I would start modifying here
@profile
def final_calc(X,Y):
    return np.matmul(X,Y)

### Is it necessary to print everything?
### 41 MiB
#@profile
#def print_res(result):
#    for r in result:
#        print(r)
#    return

#ipdb.set_trace()
X,Y = makeXY(N)
result = storing_results(N)
result = final_calc(X,Y)
print(result)


