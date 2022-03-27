# This is a sample Python script.

def karatsuba(x,y):
    if type(x) != str:
        x = str(x)

    if type(y) != str:
        y = str(y)

    if len(x) == 1 and len(y) == 1:
        return int(x) * int(y)

    m = min(int(len(x)/2), int(len(y)/2))

    a = x[:m]
    b = x[m:]
    c = y[:m]
    d = y[m:]

    z2 = karatsuba(a,c)
    z0 = karatsuba(b,d)
    z1 = karatsuba(int(a) + int(b), int(c) + int(d)) - z0 - z2

    result = z2 * 10**(m*2) + z1 * 10**(m) + z0
    return result

ret = karatsuba(33,44)
print(ret)