for n in range (1,100):
    for m in range (n+1,101):
        a=m**2-n**2
        b=2*m*n
        c=m**2+n**2
        if (a+b+c==1000):
                print ("Product is:" , a*b*c)
                break