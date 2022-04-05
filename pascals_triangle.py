# it's basically the same as binomial_coefficient.py, just written from different perspective - looking at
# the graph of pascals triangle instead of the binomial coefficient formula

import math

def pt(n, k):
    if k > n:
        return 0

    if k == n:
        return 1

    if k <= 0 or n <= 1:
        return 1

    a = pt(n-1, k)
    b = pt(n-1, k-1)

    return a + b


alg1_me = pt(4,0)
py1 = math.comb(4,2)

print(alg1_me)
print(py1)