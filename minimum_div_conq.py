# for rec 3
def min_dq(l): # gets and returns table
    l_len = len(l)

    if l_len <= 1:
        return l
    elif l_len == 2:
        if l[0] > l[1]:
            return [l[0]]
        else:
            return [l[1]]

    half = int(l_len/2)

    left = l[:half]
    right = l[half:]

    left = min_dq(left)
    right = min_dq(right)

    if left[0] > right[0]:
        return left

    else:
        return right

list_num1 = [1,3,4,2]
ret = min_dq(list_num1)

print(ret)