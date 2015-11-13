def gcdRecur(a, b):
    if b==0 :
        return a
    else:
        return gcdRecur(b,a%b)

gcdRecur(2,12)
