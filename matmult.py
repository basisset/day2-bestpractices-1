# Program to multiply two matrices using nested loops
import random
from memory_profiler import profile

N = 250

# NxN matrix

### 38 MiB
@profile
def makeX():
    X = []
    for i in range(N):
        X.append([random.randint(0,100) for r in range(N)])
    return X
# Nx(N+1) matrix

### 39 MiB
@profile
def makeY():
    Y = []
    for i in range(N):
        Y.append([random.randint(0,100) for r in range(N+1)])
    return Y
# result is Nx(N+1)

### 39 MiB
@profile
def appending_results():
    result = []
    for i in range(N):
        result.append([0] * (N+1))
    return result
    # iterate through rows of X

    ### This segment takes the most time at about 13.3487 s
    ### 41 MiB
    ### There is probably a smarter way to multiply X and Y
    ### and since these lines takes the longest then I would start modifying here
@profile
def final_calc(X,Y):
    for i in range(len(X)):
    # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result

### Is it necessary to print everything?
### 41 MiB
#@profile
#def print_res(result):
#    for r in result:
#        print(r)
#    return

X = makeX()
Y = makeY()
result = appending_results()
result = final_calc(X,Y)
#print_res(result)


