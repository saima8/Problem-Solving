while(1):
    h1,m1,h2,m2=map(int, input().split())
    if(h1==0 and m1==0 and h2==0 and m2==0):
        break
    else:
        h1=h1*60
        h2=h2*60
        if(h1==0 ):
            h1=24*60
        if(h2==0):
            h2=24*60
        sum1=h1+m1
        sum2=h2+m2
        if(sum1<sum2):
            total=sum2-sum1
        else:
            total = 24*60 - (sum1-sum2)
        print(total)