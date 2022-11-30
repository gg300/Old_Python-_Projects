def prim(n):
    i=3
    if n%2==0:
        return False
    if n<=1:
        return False
    while i*i<=n:
        if n%i==0:
            return False
        elif (n/i)%i==0:
            return False
        i+=2
    return True