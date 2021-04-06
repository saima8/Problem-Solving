num = int(input())

for i in range (num):
    text = input().split()
    word = []
    final = ''
    for j in text:
        word.append(j)
    for k in word:
        final+=k[0]
    print(final)