list1 = [3,4,7,24,18,11,1,2]
list1.sort()

def binary_search(target, l):
    print(l)
    len_l = len(l)

    if len_l == 1:
        if l[0] == target:
            return True

        else:
            return False

    middle = int(len_l/2)
    print(l[middle])

    if l[middle] == target:
        return True

    elif l[middle] > target:
        v = binary_search(target, l[:middle])

    else:
        v = binary_search(target, l[middle:])
        # print(val)

    return v

ret = binary_search(11, list1)

print(ret)