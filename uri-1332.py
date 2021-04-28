num = int(input())

for i in range(num):
    text = input()

    if ((text[0]=='t' and text[1]=='w') or (text[0]=='t' and text[2]=='o') or (text[1]=='w' and text[2]=='o')):
        print(2)
    elif (len(text) == 3):
        print(1)
       
    elif (len(text) == 5):
        print(3)
    
    