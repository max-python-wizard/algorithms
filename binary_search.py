from math import floor

list1 = [3,4,7,24,18,11,1,2,5,8,111,-1]
list1.sort()


def binary_search_rec(target, l, ran = ()):
    len_l = len(l)

    if len_l == 1:
        if l[0] == target:
            return ran[0]

        else:
            return False

    if ran == ():
        ran = (0, len_l)

    middle = int(len_l/2)
    # print(l[middle])

    if l[middle] == target:
        return ran[0] + middle

    elif l[middle] > target:
        v = binary_search_rec(target, l[:middle], (ran[0], ran[0] + middle))

    else:
        v = binary_search_rec(target, l[middle:], (ran[0] + middle, ran[1]))
        # print(val)

    return v

def binary_search(target, l):

    len_l = len(l)
    left = 0
    right = len_l


    while(right - left > 2):
        middle = left + floor((right - left) / 2)
        l_middle = l[middle]

        if l_middle == target:
            return middle

        elif target > l_middle:
            left = middle

        else:
            right = middle

    else:
        if l[left] == target:
            return left
        elif l[left+1] == target:
            return left+1
        else:
            return False

ret = binary_search_rec(4, list1)
print(ret)

ret = binary_search(4, list1)
print(ret)