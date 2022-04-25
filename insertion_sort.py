list1 = [3,4,7,24,18,11,1,2,5,8,111,-1]

def insertion_sort(l):
    temp = False
    for i in range(len(l)-1):
        l_i = l[i]
        l_i1 = l[i+1]
        l_0 = l[0]

        if l_i1 < l_i:

            if l_i1 < l_0:
                l.insert(0, l_i1)
                del l[i+2]

            else:
                for k in range(1, i+1):
                    l_ik = l[i-k]
                    if l_i1 > l_ik:
                        l.insert(i-k+1, l_i1)
                        del l[i+2]
                        break

    return l


ret = insertion_sort(list1)
print(ret)