num = int(input())
for i in range(num):
    word1, word2 = input().split()
    leng1 = len(word1)
    leng2 = len(word2)
    final1=''
    if leng1>=leng2:
        leng=leng1
    else:
        leng=leng2
    for j in range(leng):
        if j<leng1:
            final1 += word1[j]
        if j<leng2:
            final1 += word2[j]
    print(final1)
    