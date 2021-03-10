while(1):
    inp = input()
    if (inp=="*"):
        break
    sentence = inp.split(" ")
    temp=[]
    for word in sentence:
        if word != '':
            temp.append(word)
    sentence=temp
    matched=True
    for i in range(len(sentence)-1):
        if sentence[i][0].lower() != sentence[i+1][0].lower():
            matched= False
            break
    if not matched:
        print("N")
    else:
        print("Y")