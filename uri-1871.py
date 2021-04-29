while True:
    a, b = map(int, input().split())
    if (a == 0 and b == 0):
        break
    sum = a + b
    strSum = str(sum)
    print(strSum.replace('0', ''))