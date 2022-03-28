from random import randint as randint

def merge_sort(array_):

    if len(array_) < 2:
        return array_

    middle = int(len(array_)/2)

    left = array_[:middle]
    right = array_[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    array_sorted = []
    j = 0
    k = 0

    for i in range(len(array_)):
        if j >= len(left):
            array_sorted.append(right[k])
            k += 1

        elif k >= len(right):
            array_sorted.append(left[j])
            j += 1

        elif left[j] < right[k]:
            array_sorted.append(left[j])
            j += 1

        else:
            array_sorted.append(right[k])
            k += 1

    return array_sorted


array1 = [3, 6, 6, 2, 7, 4]
print(array1)
print(merge_sort(array1))

array2 = []
for i in range(20):
    array2.append(randint(0, 100))

print(array2)
print(merge_sort(array2))