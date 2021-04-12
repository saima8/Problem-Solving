while True:
    bank, deben = input().split()
    if bank == deben == '0':
        break
    r = [int(x) for x in input().split()]
    for i in range(int(deben)):
        d, c, v = input().split()
        r[int(d)-1] -= int(v)
        r[int(c)-1] += int(v)
    bailout = 'S'
    for i in r:
        if int(i) < 0:
            bailout = 'N'
            break
    print(bailout)