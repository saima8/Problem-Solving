while True:
    try:

        alice, beto, clara = map(int, input().split())
        
        if (alice == beto) and (beto == clara):
            print('*')
        elif beto == clara:
            print('A')
        elif alice == clara:
            print('B')
        elif alice == beto:
            print('C')


    except EOFError:
        break