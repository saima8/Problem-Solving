while True:
    left, right = map(int, input().split())
    if (left == 0 and right == 0):
        break
    
    print(left + right)