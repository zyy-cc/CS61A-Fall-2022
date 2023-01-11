import torch
from turboaeStuff import turboaeBinaryBlock1, turboaeBinaryBlock2, turboaeBinaryBlock3
from turboaeStuff import turboaeConBlock1, turboaeConBlock2, turboaeConBlock3
import numpy as np
import itertools as it

# dev = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

# Create a num_query of 512 random input vectors of 0,1
X = torch.randint(0, 2, (512, 100)).float()
# Change 0,1 to -1,1
X = X * 2 - 1

# print(X.shape)
# print(X)

# get output# 10 of turboAE Binary's Block 1 on the inputs X
Y = turboaeBinaryBlock1(X, outIndex=10)


# Y.shape
# print(Y.shape)
# print(Y)

# turboaeBinaryBlock2(X, outIndex=10)
# turboaeBinaryBlock3(X, outIndex=10)
# turboaeConBlock1(X, outIndex=10)
# turboaeConBlock2(X, outIndex=10)
# turboaeConBlock3(X, outIndex=10)

# generate a num_query of input vectors. num_query size here is 512
def generate_data(num_query, n, k):
    """
    Input num_query, the length of input sequence
    Output w, w', x
    """
    w = torch.randint(0, 2, (num_query, k)).float()
    w_two = torch.randint(0, 2, (num_query, k)).float()
    x = torch.randint(0, 2, (num_query, n - k)).float()
    w, w_two, x = 2 * w - 1, 2 * w_two - 1, 2 * x - 1
    return w, w_two, x


def query_func(func, w, w_two, x, s, outIndex):
    """
    Input w, w',x,s
    Output f(w,x) * f(w',x) * ws * ws' [num_query,1]
    """
    seq1 = torch.cat((w, x), 1)
    seq2 = torch.cat((w_two, x), 1)
    fproduct = func(seq1, outIndex) * func(seq2, outIndex)
    fproduct = fproduct.float()
    fproduct = fproduct.to('cpu')

    ws, ws_two = 1, 1
    for i in range(len(s)):
        if s[i] == 1:
            ws *= w[:, i]
            ws_two *= w_two[:, i]

    return fproduct * ws * ws_two


def estimate(B, n, k, num_query, func, outIndex):
    """
    B is the indicator string
    n is the length of total bits
    k is the length of partiton I
    num_query is the number of queries
    func refers to the function
    Return the estimate W(S)
    """
    s = B[:k]  # (0,1,...,k-1)
    w, w_two, x = generate_data(num_query, n, k)
    res = query_func(func, w, w_two, x, s, outIndex)
    res = res.float()
    mean_val = torch.mean(res, 0)
    return mean_val


def delete_duplicate(listA):
    """
    Delete the duplicate in listA.
    """
    resultList = []
    for item in listA:
        if not item in resultList:
            resultList.append(item)
    return resultList


def Goldreich_Levin(func, n, num_set, gamma, num_query, outindex):
    """
    num_query is the number of queries
    outindex is the position of the output bit, start from 0
    gamma is the parameter that needs to be specified.
    return the list which contains the higher Fourier weight.
    """
    # Initialize the L set
    L = np.random.randint(0, 2, (num_set, n))
    for k in range(1, n):
        new_set = []
        [rows, cols] = L.shape
        for i in range(rows):
            S = list(L[i, :])
            b0, b1 = S.copy(), S.copy()
            b0[k], b1[k] = 0, 1
            w0, w1 = estimate(b0, n, k, num_query, func, outindex), estimate(b1, n, k, num_query, func, outindex)
            if w0 >= gamma ** 2 / 4:
                new_set.append(b0)
            if w1 >= gamma ** 2 / 4:
                new_set.append(b1)
        L = delete_duplicate(new_set)
        if len(L) <= 1:
            break
        L = np.array(L)
    return L


num_querys = [10, 15, 20, 25]
gamma3s = [0.01, 0.05, 0.1]
num_sets = [2, 5, 10, 15]

for query in range(1, 11):
    for gamma in range(1, 11):
        print("Block3: num_set={}, gamma = {}, num_query= {}, outindex = {}".format(5, gamma/100, query, 10))
        L3 = Goldreich_Levin(turboaeBinaryBlock3, n=100, num_set=5, gamma = gamma/100, num_query=query, outindex=10)
        print("L2: {}".format(L3))

# for query in num_querys:
#     for set in num_sets:
#         # Block1
#         print("Block1: num_set={}, gamma = {}, num_query= {}, outindex = {}".format(set, 0.75, query, 10))
#         L1 = Goldreich_Levin(turboaeBinaryBlock1, n=100, num_set=set, gamma = 0.75, num_query=query, outindex = 10)
#         print("L1: {}".format(L1))
#         # Block2
#         print("Block2: num_set={}, gamma = {}, num_query= {}, outindex = {}".format(set, 0.75, query, 10))
#         L2 = Goldreich_Levin(turboaeBinaryBlock2, n=100, num_set=set, gamma = 0.75, num_query=query, outindex = 10)
#         print("L2: {}".format(L2))
#         # Block3

#         print("Block3: num_set={}, gamma = {}, num_query= {}, outindex = {}".format(set, 0.05, query, 10))
#         L3 = Goldreich_Levin(turboaeBinaryBlock3, n=100, num_set=set, gamma = 0.05, num_query=query, outindex = 10)
#         print("L3: {}".format(L3))

