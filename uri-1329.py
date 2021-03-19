while(1):
    sum1=0
    sum2=0
    num=int(input())
    if (num==0):
        break
    else:
        matches=list(map(int, input().split()))
        for ele in matches:
            if ele==0:
                sum1+=1
            else:
                sum2+=1
        
    print(f"Mary won {sum1} times and John won {sum2} times")