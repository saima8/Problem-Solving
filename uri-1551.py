testCase = int(input())

for i in range (testCase):
    sentence = input()
    total = []

    for i in sentence:
        if i not in total:
           total.append(i)
    
    for j in total:
        if j== ' ':
            total.remove(j)
        elif j== ',':
            total.remove(j)

    if (len(total) == 26):
        print('frase completa')
    elif (len(total) > 13):
        print('frase quase completa')
    else:
        print('frase mal elaborada')