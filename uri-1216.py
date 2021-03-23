count=0
sum=0
while (1):
  
    try: 
        name = input()
        dis = input()

        count+=1
        sum+=int(dis)
    except EOFError:
        break

avg = float(sum/count)
print("{:.1f}".format(avg))