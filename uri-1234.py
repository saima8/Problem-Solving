sentence = input()
while (1):
    try:    
        final=''
        count=0

        for ch in sentence:
            if ch==' ':
                final+=ch
            else:
                count+=1
                if count%2!=0:
                    final+=ch.upper()
                else:
                    final+=ch.lower()
        
        print(final)
        
        sentence = input()
    except EOFError:
        break