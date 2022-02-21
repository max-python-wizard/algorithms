sequence = [1,3,4,2]
#%%
# for i in range(2,len(sequence)):
#%%

## funciton finding all growing subsequences from this point
def find_further(seq, start, previous_subs = []):
    print("running fund further")
    print(f"previous {previous_subs}")
    start_el = seq[start]
    seq_len = len(seq)
    # previous_subs.append(seq[start])

    previous = previous_subs.copy()
    previous.append(seq[start])

    if start+1 >= seq_len:
        # previous_subs.append(seq[start+1])
        return previous

    return_subs = []
    any_bigger = False
    for i in range(start+1, len(seq)):

        i_el = seq[i]

        if i_el > start_el:
            # previous_subs.append(seq[i])
            any_bigger = True
            ret = find_further(seq, i, previous)
            if ret != []:
                return_subs.append(ret)

    if any_bigger == False:
        return previous

    return return_subs
#%%
# r = find_further(sequence, 0)
#
# print(r)
#
# def max_length()



#
# def longest_growing_substring_length(n: int, tab: list) -> int:
#     mx = 1
#     length = 1
#
#     for i in range(1, n):
#         if tab[i] > tab[i - 1]:
#             length += 1
#             if length > mx:
#                 mx = length
#         else:
#             length = 1
#
#     return mx
#
# tab = [4, 9, 7, 2, 4, 7, 9, 3, 8, 6]
# n = 10
#
# result = longest_growing_substring_length(n, tab)
# print(result)

## Fał
def largest_subsequence(seq):
    subsequences = []
    max_length = []
    max_length.insert(0, 1)
    subsequences.insert(seq[0])
    for i in range(1, len(seq)):
        max_tmp = 1

        for k in range(0, i):
            if(seq[k] < seq[i]):
                max_tmp = max(max_tmp, max_length[k] + 1)

        max_length.insert(i, max_tmp)

    return max(max_length)

length = largest_subsequence(sequence)

print(length)