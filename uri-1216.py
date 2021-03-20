
while (1):
    count=0
    sum=0
    name = input()
    dis = int(input()) 
    try:    
        
        count+=1
        sum+=dis
        
                 
    except ValueError:
        break
avg = float(sum/count)
print(avg)