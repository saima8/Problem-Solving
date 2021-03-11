while(1):
    num = int(input())
    if num == 0:
        break
    for i in range(num):
        rectangles = list(map(int, input().split()))
        black = []
        for each in rectangles:
            if each <= 127:
                black.append(each)
        if len(black) == 1:
            for i in range(len(rectangles)):
                if black[0] == rectangles[i]:
                    if i == 0:
                        print("A")
                    if i == 1:
                        print("B")
                    if i == 2:
                        print("C")
                    if i == 3:
                        print("D")
                    if i == 4:
                        print("E")
        else:
            print("*")