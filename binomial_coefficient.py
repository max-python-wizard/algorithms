import math

# n > k
i = 0


def bc(n, k):
    global i
    print(f"loop {i}")
    if k == n or k == 0:
        return 1

    a = bc(n-1, k-1)
    b = bc(n-1, k)

    i += 1
    return a + b

alg1_me = bc(20,4)
py1 = math.comb(20,4)

print(alg1_me)
print(py1)