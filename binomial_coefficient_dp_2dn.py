# I implement binomial coefficient calculation using dynamic programming
# In dynamic programming you save (remember) results through iteration/recursion so that calls
# with the same arguments won't be calculated more then one time.

# I could implement table as a global variable, but to avoid that I pass the table down around
# and it's updated as it goes through recursive calls.

import math
import numpy as np


def dynamic_wrapper(n, k):
    table = np.zeros((n+1, k+1))

    result, table = bc_dynamic(n, k, table)

    return result

def bc_dynamic(n, k, table):
    if k == n or k == 0:
        table[n, k] = 1
        return 1, table

    if table[n, k] != 0:
        return table[n, k], table

    a, table = bc_dynamic(n-1, k-1, table)
    b, table = bc_dynamic(n-1, k, table)

    result = a + b
    table[n, k] = result

    return result, table

def bc(n, k):
    if k == n or k == 0:
        return 1

    a = bc(n-1, k-1)
    b = bc(n-1, k)

    return a + b


alg1 = bc(4,3)
dynamic = dynamic_wrapper(4,3)
py1 = math.comb(4,3)

print(alg1)
print(dynamic)
print(py1)