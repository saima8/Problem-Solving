while True:
    tickets, people = map(int, input().split())

    if (tickets == 0 and people == 0):
        break

    demo = []

    total = 0

    x = [int(x) for x in input().split()]

    for i in range (len(x)):
        if x[i] in demo:
            total += 1
        else:
            demo.append(x[i])
    print(total)