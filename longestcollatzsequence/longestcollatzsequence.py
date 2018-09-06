

def func():
    mxch = 0
    for i in range(13, 1000000):
        ch = 1
        n = i
        while n != 1:
            if n%2 == 0:
                n = n/2
            else:
                n = (3*n)+1
            ch+=1
        else:
            if ch > mxch:
                mxch = ch
                print(mxch)
    return(mxch)

print(func())



