firstTestCase = True
while (True):
    
    num = int(input())
    if num == 0:
        break
    
    if not firstTestCase:
        print("")

    texts = []
    maxLength = 0

    for i in range(num):
        text = input()
        texts.append(text)

        if len(text) > maxLength:
            maxLength = len(text)

    for word in texts:
        spaces = maxLength - len(word)
        updatedWord = ' ' * spaces + word
        print(updatedWord)

    firstTestCase = False


    



#while(1):
#     num=int(input())
#     if num==0:
#         break
#     initial = 0
#     texts=[]
#     for i in range (num):
#         text=input()
#         texts.append(text)
#         if len(text)>initial:
#             initial=len(text)
#     for word in texts:
#         updated=''
#         spaces = initial - len(word)
#         for i in range (spaces):
#             updated+=' '
#         updated+=word
#         print(updated)