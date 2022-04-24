list1 = [3,4,7,24,18,11,1,2,5,8,111,-1]
list1.sort()

def binary_search(target, l, ran = ()):
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
        v = binary_search(target, l[:middle], (ran[0], ran[0] + middle))

    else:
        v = binary_search(target, l[middle:], (ran[0] + middle, ran[1]))
        # print(val)

    return v

ret = binary_search(24, list1)

print(ret)