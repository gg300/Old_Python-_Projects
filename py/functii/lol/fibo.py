def fibo(n):
    a=1
    b=1
    for i in range(n):
        if a<b:
            print("",a)
            a+=b
        else:
            print("",b)
            b+=a