from random import randint

def quicksort(list_):

    # if len(list_)
    if len(list_) <= 1:
        return list_

    if len(list_) < 3:
        if list_[0] > list_[1]:
            return [list_[1]] + [list_[0]]
        else:
            return list_

    pivot = int(len(list_)/2)
    # randint(0, len(list_))
    # len(list_) - 1

    list_, pivot_location = partition(list_, pivot)

    left = quicksort(list_[:pivot_location])
    right = quicksort(list_[pivot_location:])

    list_ = left + right

    return list_

def partition(list_, pivot):
    left = []
    right = []

    pivot_value = list_[pivot]

    for el in list_:
        if el < pivot_value:
            left.append(el)
        elif el > pivot_value:
            right.append(el)

    left.append(pivot_value)
    return left + right, len(left)

def partition_mixed(list_, pivot):

    i = 0
    j = len(list_) - 1

    # last_swap = 0
    while(i < j):
        while(list_[i] < list_[pivot]): i += 1
        while(list_[j] >= list_[pivot]): j -= 1
        # if i == pivot:
        #     i +=1
        if (i < j):
            list_ = swap(i, j, list_)
            # last_swap = j

    list_ = swap(i, pivot, list_)
    return list_, i

def swap(i, j, list_):
    temp = list_[i]
    list_[i] = list_[j]
    list_[j] = temp

    return list_

# list1 = [1,4,6,3,9,5]
# ret = quicksort(list1)

list2 = [1,4,6,3,9,2,5]
ret = quicksort(list2)

print(ret)