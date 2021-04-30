while True:
    testCase = int(input())
    if (testCase == 0):
        break
    player1 = 0
    player2 = 0

    for i in range (testCase):
        play1, play2 = map(int, input().split())
        if (play1 > play2):
            player1 += 1
        elif (play1 == play2):
            player1 += 0
            player2 += 0
        else:
            player2 +=1

    print(player1, player2)