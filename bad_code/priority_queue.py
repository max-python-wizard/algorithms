from array import *
from math import log2
from math import pow
from math import floor

array1 = array('B', [3,4,7,24,18,11,1,2,5,8,111])

def find_parent(n):

    if n == 0:
        return -1

    elif n == 1 or n == 2:
        return 0

    level = floor(log2(n+1))
    level_above = int(pow(2, level-1))-1

    this_level = int(pow(2,level))-1
    above_n = n - this_level

    parent = level_above + floor(above_n/2)

    return parent

def find_children(n):

    level = floor(log2(n+1))

    this_level = pow(2,x)-1
    level_below = pow(2, x+1)-1

    above_n = n - this_level

    children = (level_below + above_n*2, level_below + above_n*2 +1)

    return children

def add_node(pq, k):
    len_heap = len(pq)
    loc_k = len_heap

    pq.insert(loc_k, k)

    parent = find_parent(loc_k)
    while k > pq[parent]:
        temp = pq[parent]
        pq[parent] = k
        pq[loc_k] = temp
        loc_k = parent
    return pq


print(pq1_max)
#%%
add_node(pq1_max, 1)
#%%
add_node(pq1_max, 11)

print(array1[0])
print(print(find_parent(6)))