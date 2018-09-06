import math

def func():
    su = {0}
    for i in range(1, 10000):
        b = 0
        for j in range(1, i):
            if i%j == 0:
                b += j
        else:
            a = 0
            for k in range(1, b):
                if b%k == 0:
                    a += k
            else:
                if a == b:
                    su.update([a,b])
    else:
        return sum(su)

print(func())



