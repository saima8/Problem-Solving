while(1):
    num=int(input())
    if num==0:
        break
    initial = 0
    texts=[]
    for i in range (num):
        text=input()
        texts.append(text)
        if len(text)>initial:
            initial=len(text)
    for word in texts:
        updated=''
        spaces = initial - len(word)
        for i in range (spaces):
            updated+=' '
        updated+=word
        print(updated)