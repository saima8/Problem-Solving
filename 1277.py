num = int(input())

while True:
    if num == 0:
        break
    term = int(input())
    studentNames = list(input().split())
    attendance = list(input().split())
    

    for i in range (len(studentNames)):
        for attendance[i] in attendance:
            countA = attendance[i].count('A')
            if countA >1 :
                print(studentNames[i])
                # j+=1
            elif len(attendance)==1 and countA<2:
                break
        
    