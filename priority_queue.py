from array import *
from math import log2
from math import pow
from math import floor

array1 = array('B', [3,4,7,24,18,11,1,2,5,8,111])

def find_parent(n):

    if n <= 0:
        return -1

    elif n == 1 or n == 2:
        return 0
    else:
        parent = floor((n-1)/2)

    return parent

def find_children(n):

    x = n * 2
    children = (x+1, x+2)

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

def find_depth(pq):
    len_pq = len(pq)

    depth = floor(log2(len_pq + 1))

    return depth

def print_pq(pq):
    len_pq = len(pq)

    depth = find_depth(pq)
    current_node = 0

    margin = int(pow(2, depth)) #int(depth/2)
    for i in range(depth+1):
        nodes_at_level = int(pow(2, i))

        if current_node >= len_pq:
            break

        m = ' ' * margin
        print(m, end=" ")
        margin -= 2
        len_level = 2 * depth
        m_level = "" * len_level
        for k in range(nodes_at_level):

            if current_node >= len_pq:
                break

            print(pq[current_node], m_level, end="")
            current_node += 1
            len_level /= 2

        print()

    return

# print(pq1_max)
# #%%
# add_node(pq1_max, 1)
# #%%
# add_node(pq1_max, 11)

# print(array1[0])
# print(find_children(4))
#
# print(find_depth(array1))

print_pq(array1)